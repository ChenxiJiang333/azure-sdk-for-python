#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

"""
Example to show managing subscription entities under a ServiceBus namespace, including
    - Create a subscription
    - Get subscription properties and runtime information
    - Update a subscription
    - Delete a subscription
    - List subscriptions under the given ServiceBus Namespace
"""

import os
import asyncio
import uuid
from azure.servicebus.aio.management import ServiceBusAdministrationClient
from azure.identity.aio import DefaultAzureCredential

FULLY_QUALIFIED_NAMESPACE = os.environ["SERVICEBUS_FULLY_QUALIFIED_NAMESPACE"]
TOPIC_NAME = os.environ["SERVICEBUS_TOPIC_NAME"]
SUBSCRIPTION_NAME = "sb_mgmt_sub" + str(uuid.uuid4())


async def create_subscription(servicebus_mgmt_client):
    print("-- Create Subscription")
    await servicebus_mgmt_client.create_subscription(TOPIC_NAME, SUBSCRIPTION_NAME)
    print("Subscription {} is created.".format(SUBSCRIPTION_NAME))
    print("")


async def delete_subscription(servicebus_mgmt_client):
    print("-- Delete Subscription")
    await servicebus_mgmt_client.delete_subscription(TOPIC_NAME, SUBSCRIPTION_NAME)
    print("Subscription {} is deleted.".format(SUBSCRIPTION_NAME))
    print("")


async def list_subscriptions(servicebus_mgmt_client):
    print("-- List Subscriptions")
    async for subscription_properties in servicebus_mgmt_client.list_subscriptions(TOPIC_NAME):
        print("Subscription Name:", subscription_properties.name)
    print("")


async def get_and_update_subscription(servicebus_mgmt_client):
    print("-- Get and Update Subscription")
    subscription_properties = await servicebus_mgmt_client.get_subscription(TOPIC_NAME, SUBSCRIPTION_NAME)
    print("Subscription Name:", subscription_properties.name)
    print("Please refer to SubscriptionDescription for complete available settings.")
    print("")
    # update by updating the properties in the model
    subscription_properties.max_delivery_count = 5
    await servicebus_mgmt_client.update_subscription(TOPIC_NAME, subscription_properties)

    # update by passing keyword arguments
    subscription_properties = await servicebus_mgmt_client.get_subscription(TOPIC_NAME, SUBSCRIPTION_NAME)
    await servicebus_mgmt_client.update_subscription(TOPIC_NAME, subscription_properties, max_delivery_count=3)


async def get_subscription_runtime_properties(servicebus_mgmt_client):
    print("-- Get Subscription Runtime Properties")
    get_subscription_runtime_properties = await servicebus_mgmt_client.get_subscription_runtime_properties(
        TOPIC_NAME, SUBSCRIPTION_NAME
    )
    print("Subscription Name:", get_subscription_runtime_properties.name)
    print("Please refer to SubscriptionRuntimeProperties from complete available runtime properties.")
    print("")


async def main():
    credential = DefaultAzureCredential()
    async with ServiceBusAdministrationClient(FULLY_QUALIFIED_NAMESPACE, credential) as servicebus_mgmt_client:
        await create_subscription(servicebus_mgmt_client)
        await list_subscriptions(servicebus_mgmt_client)
        await get_and_update_subscription(servicebus_mgmt_client)
        await get_subscription_runtime_properties(servicebus_mgmt_client)
        await delete_subscription(servicebus_mgmt_client)


asyncio.run(main())
