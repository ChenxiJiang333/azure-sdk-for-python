# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
# pylint: disable=wrong-import-position

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._patch import *  # pylint: disable=unused-wildcard-import

from ._operations import Operations  # type: ignore
from ._bare_metal_machines_operations import BareMetalMachinesOperations  # type: ignore
from ._cloud_services_networks_operations import CloudServicesNetworksOperations  # type: ignore
from ._cluster_managers_operations import ClusterManagersOperations  # type: ignore
from ._clusters_operations import ClustersOperations  # type: ignore
from ._kubernetes_clusters_operations import KubernetesClustersOperations  # type: ignore
from ._l2_networks_operations import L2NetworksOperations  # type: ignore
from ._l3_networks_operations import L3NetworksOperations  # type: ignore
from ._rack_skus_operations import RackSkusOperations  # type: ignore
from ._racks_operations import RacksOperations  # type: ignore
from ._storage_appliances_operations import StorageAppliancesOperations  # type: ignore
from ._trunked_networks_operations import TrunkedNetworksOperations  # type: ignore
from ._virtual_machines_operations import VirtualMachinesOperations  # type: ignore
from ._volumes_operations import VolumesOperations  # type: ignore
from ._bare_metal_machine_key_sets_operations import BareMetalMachineKeySetsOperations  # type: ignore
from ._bmc_key_sets_operations import BmcKeySetsOperations  # type: ignore
from ._metrics_configurations_operations import MetricsConfigurationsOperations  # type: ignore
from ._agent_pools_operations import AgentPoolsOperations  # type: ignore
from ._kubernetes_cluster_features_operations import KubernetesClusterFeaturesOperations  # type: ignore
from ._consoles_operations import ConsolesOperations  # type: ignore

from ._patch import __all__ as _patch_all
from ._patch import *
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "Operations",
    "BareMetalMachinesOperations",
    "CloudServicesNetworksOperations",
    "ClusterManagersOperations",
    "ClustersOperations",
    "KubernetesClustersOperations",
    "L2NetworksOperations",
    "L3NetworksOperations",
    "RackSkusOperations",
    "RacksOperations",
    "StorageAppliancesOperations",
    "TrunkedNetworksOperations",
    "VirtualMachinesOperations",
    "VolumesOperations",
    "BareMetalMachineKeySetsOperations",
    "BmcKeySetsOperations",
    "MetricsConfigurationsOperations",
    "AgentPoolsOperations",
    "KubernetesClusterFeaturesOperations",
    "ConsolesOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
