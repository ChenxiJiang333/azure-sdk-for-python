# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
import threading
import uuid
from typing import Any, Callable, cast, Optional

from azure.core.exceptions import ResourceNotFoundError, HttpResponseError
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpTransport
from azure.core.polling import PollingMethod, LROPoller, NoPolling

from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.common import with_current_context


class KeyVaultOperationPoller(LROPoller):
    """Poller for long running operations where calling result() doesn't wait for operation to complete.

    :param polling_method: The poller's polling method.
    :type polling_method: ~azure.core.polling.PollingMethod
    """

    def __init__(self, polling_method: PollingMethod) -> None:
        super(KeyVaultOperationPoller, self).__init__(None, None, lambda *_: None, NoPolling())
        self._polling_method = polling_method

    # pylint: disable=arguments-differ
    def result(self) -> "Any":  # type: ignore
        """Returns a representation of the final resource without waiting for the operation to complete.

        :returns: The deserialized resource of the long running operation
        :rtype: Any

        :raises ~azure.core.exceptions.HttpResponseError: Server problem with the query.
        """
        return self._polling_method.resource()

    @distributed_trace
    def wait(self, timeout: Optional[float] = None) -> None:
        """Wait on the long running operation for a number of seconds.

        You can check if this call has ended with timeout with the "done()" method.

        :param float timeout: Period of time to wait for the long running operation to complete (in seconds).

        :raises ~azure.core.exceptions.HttpResponseError: Server problem with the query.
        """

        if not self._polling_method.finished():
            self._done = threading.Event()
            self._thread = threading.Thread(
                target=with_current_context(self._start), name=f"KeyVaultOperationPoller({uuid.uuid4()})"
            )
            self._thread.daemon = True
            self._thread.start()

        if self._thread is None:
            return
        self._thread.join(timeout=timeout)
        try:
            # Let's handle possible None in forgiveness here
            raise self._exception  # type: ignore
        except TypeError:  # Was None
            pass


class DeleteRecoverPollingMethod(PollingMethod):
    """Poller for deleting resources, and recovering deleted resources, in vaults with soft-delete enabled.

    This works by polling for the existence of the deleted or recovered resource. When a resource is deleted, Key Vault
    immediately removes it from its collection. However, the resource will not immediately appear in the deleted
    collection. Key Vault will therefore respond 404 to GET requests for the deleted resource; when it responds 2xx,
    the resource exists in the deleted collection i.e. its deletion is complete.

    Similarly, while recovering a deleted resource, Key Vault will respond 404 to GET requests for the non-deleted
    resource; when it responds 2xx, the resource exists in the non-deleted collection, i.e. its recovery is complete.

    :param pipeline_response: The operation's original pipeline response.
    :type pipeline_response: PipelineResponse
    :param command: A callable to invoke when polling.
    :type command: Callable
    :param final_resource: The final resource returned by the polling operation.
    :type final_resource: Any
    :param bool finished: Whether or not the polling operation is completed.
    :param int interval: The polling interval, in seconds.
    """

    def __init__(
        self,
        pipeline_response: PipelineResponse,
        command: Callable,
        final_resource: Any,
        finished: bool,
        interval: int = 2,
    ) -> None:
        self._pipeline_response = pipeline_response
        self._command = command
        self._resource = final_resource
        self._polling_interval = interval
        self._finished = finished

    def _update_status(self) -> None:
        try:
            self._command()
            self._finished = True
        except ResourceNotFoundError:
            pass
        except HttpResponseError as e:
            # If we are polling on get_deleted_* and we don't have get permissions, we will get
            # ResourceNotFoundError until the resource is recovered, at which point we'll get a 403.
            if e.status_code == 403:
                self._finished = True
            else:
                raise

    def initialize(self, client: Any, initial_response: Any, deserialization_callback: Callable) -> None:
        pass

    def run(self) -> None:
        while not self.finished():
            self._update_status()
            if not self.finished():
                # We should always ask the client's transport to sleep, instead of sleeping directly
                transport: HttpTransport = cast(HttpTransport, self._pipeline_response.context.transport)
                transport.sleep(self._polling_interval)

    def finished(self) -> bool:
        return self._finished

    def resource(self) -> Any:
        return self._resource

    def status(self) -> str:
        return "finished" if self._finished else "polling"
