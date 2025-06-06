# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.apimanagement import ApiManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestApiManagementApiTagDescriptionOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(ApiManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_api_tag_description_list_by_service(self, resource_group):
        response = self.client.api_tag_description.list_by_service(
            resource_group_name=resource_group.name,
            service_name="str",
            api_id="str",
            api_version="2024-05-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_api_tag_description_get_entity_tag(self, resource_group):
        response = self.client.api_tag_description.get_entity_tag(
            resource_group_name=resource_group.name,
            service_name="str",
            api_id="str",
            tag_description_id="str",
            api_version="2024-05-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_api_tag_description_get(self, resource_group):
        response = self.client.api_tag_description.get(
            resource_group_name=resource_group.name,
            service_name="str",
            api_id="str",
            tag_description_id="str",
            api_version="2024-05-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_api_tag_description_create_or_update(self, resource_group):
        response = self.client.api_tag_description.create_or_update(
            resource_group_name=resource_group.name,
            service_name="str",
            api_id="str",
            tag_description_id="str",
            parameters={"description": "str", "externalDocsDescription": "str", "externalDocsUrl": "str"},
            api_version="2024-05-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_api_tag_description_delete(self, resource_group):
        response = self.client.api_tag_description.delete(
            resource_group_name=resource_group.name,
            service_name="str",
            api_id="str",
            tag_description_id="str",
            if_match="str",
            api_version="2024-05-01",
        )

        # please add some check logic here by yourself
        # ...
