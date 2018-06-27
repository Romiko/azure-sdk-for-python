# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.configurations_operations import ConfigurationsOperations
from .operations.recommendations_operations import RecommendationsOperations
from .operations.operations import Operations
from .operations.suppressions_operations import SuppressionsOperations
from . import models


class AdvisorManagementClientConfiguration(AzureConfiguration):
    """Configuration for AdvisorManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(AdvisorManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-advisor/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class AdvisorManagementClient(SDKClient):
    """REST APIs for Azure Advisor

    :ivar config: Configuration for client.
    :vartype config: AdvisorManagementClientConfiguration

    :ivar configurations: Configurations operations
    :vartype configurations: azure.mgmt.advisor.operations.ConfigurationsOperations
    :ivar recommendations: Recommendations operations
    :vartype recommendations: azure.mgmt.advisor.operations.RecommendationsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.advisor.operations.Operations
    :ivar suppressions: Suppressions operations
    :vartype suppressions: azure.mgmt.advisor.operations.SuppressionsOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = AdvisorManagementClientConfiguration(credentials, subscription_id, base_url)
        super(AdvisorManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2018-01-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.configurations = ConfigurationsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.recommendations = RecommendationsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.suppressions = SuppressionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
