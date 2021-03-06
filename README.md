![Tests](https://github.com/smtpcom/smtpcom-python/workflows/Tests/badge.svg)
[![codecov](https://codecov.io/gh/smtpcom/smtpcom-python/branch/master/graph/badge.svg?token=W94ELHX7QD)](https://codecov.io/gh/smtpcom/smtpcom-python)
# smtp
SMTP.com Public API v4

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

```sh
pip install smtpcom
```

Then import the package:
```python
import smtpcom
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function

import time
import smtpcom
from smtpcom.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.smtp.com
# See configuration.py for a list of all supported configuration parameters.
configuration = smtpcom.Configuration(
    host = "https://api.smtp.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiID
configuration = smtpcom.Configuration(
    host = "https://api.smtp.com",
    api_key = {
        'apiID': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiID'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = smtpcom.Configuration(
    host = "https://api.smtp.com",
    api_key = {
        'apiKey': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure HTTP basic authorization: basicAuth
configuration = smtpcom.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)


# Enter a context with an instance of the API client
with smtpcom.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = smtpcom.APIKeysApi(api_client)
    api_key = 'api_key_example' # str | API Key Identificator.

    try:
        # Get API Key Details
        api_response = api_instance.get_api_key(api_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling APIKeysApi->get_api_key: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *https://api.smtp.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*APIKeysApi* | [**get_api_key**](docs/APIKeysApi.md#get_api_key) | **GET** /v4/api_keys/{api_key} | Get API Key Details
*APIKeysApi* | [**v4_api_keys_api_key_delete**](docs/APIKeysApi.md#v4_api_keys_api_key_delete) | **DELETE** /v4/api_keys/{api_key} | Delete an API Key
*APIKeysApi* | [**v4_api_keys_api_key_patch**](docs/APIKeysApi.md#v4_api_keys_api_key_patch) | **PATCH** /v4/api_keys/{api_key} | Update API Key
*APIKeysApi* | [**v4_api_keys_get**](docs/APIKeysApi.md#v4_api_keys_get) | **GET** /v4/api_keys/ | List All API Keys
*APIKeysApi* | [**v4_api_keys_post**](docs/APIKeysApi.md#v4_api_keys_post) | **POST** /v4/api_keys/ | Create a New API Key
*AccountApi* | [**v4_account_contact_patch**](docs/AccountApi.md#v4_account_contact_patch) | **PATCH** /v4/account/contact | Update Account Details
*AccountApi* | [**v4_account_get**](docs/AccountApi.md#v4_account_get) | **GET** /v4/account/ | Get Account Details
*AlertsApi* | [**v4_alerts_alert_id_delete**](docs/AlertsApi.md#v4_alerts_alert_id_delete) | **DELETE** /v4/alerts/{alert_id} | Delete Alert
*AlertsApi* | [**v4_alerts_alert_id_get**](docs/AlertsApi.md#v4_alerts_alert_id_get) | **GET** /v4/alerts/{alert_id} | Get Alert Details
*AlertsApi* | [**v4_alerts_alert_id_patch**](docs/AlertsApi.md#v4_alerts_alert_id_patch) | **PATCH** /v4/alerts/{alert_id} | Update Alert Details
*AlertsApi* | [**v4_alerts_get**](docs/AlertsApi.md#v4_alerts_get) | **GET** /v4/alerts/ | List All Allerts
*AlertsApi* | [**v4_alerts_post**](docs/AlertsApi.md#v4_alerts_post) | **POST** /v4/alerts/ | Create New Alert
*CallbacksApi* | [**v4_callbacks_delete**](docs/CallbacksApi.md#v4_callbacks_delete) | **DELETE** /v4/callbacks/ | Delete All Callbacks
*CallbacksApi* | [**v4_callbacks_event_delete**](docs/CallbacksApi.md#v4_callbacks_event_delete) | **DELETE** /v4/callbacks/{event} | Delete Callback
*CallbacksApi* | [**v4_callbacks_event_get**](docs/CallbacksApi.md#v4_callbacks_event_get) | **GET** /v4/callbacks/{event} | Get Callback Details
*CallbacksApi* | [**v4_callbacks_event_patch**](docs/CallbacksApi.md#v4_callbacks_event_patch) | **PATCH** /v4/callbacks/{event} | Update Callback Details
*CallbacksApi* | [**v4_callbacks_event_post**](docs/CallbacksApi.md#v4_callbacks_event_post) | **POST** /v4/callbacks/{event} | Create Callback
*CallbacksApi* | [**v4_callbacks_get**](docs/CallbacksApi.md#v4_callbacks_get) | **GET** /v4/callbacks/ | List All Callbacks
*CallbacksApi* | [**v4_callbacks_log_get**](docs/CallbacksApi.md#v4_callbacks_log_get) | **GET** /v4/callbacks/log | View Callback Logs
*ChannelsApi* | [**get_sender**](docs/ChannelsApi.md#get_sender) | **GET** /v4/channels/{name} | Get Channel Details
*ChannelsApi* | [**v4_channels_get**](docs/ChannelsApi.md#v4_channels_get) | **GET** /v4/channels/ | Get All Channels
*ChannelsApi* | [**v4_channels_name_delete**](docs/ChannelsApi.md#v4_channels_name_delete) | **DELETE** /v4/channels/{name} | Delete a Channel
*ChannelsApi* | [**v4_channels_name_patch**](docs/ChannelsApi.md#v4_channels_name_patch) | **PATCH** /v4/channels/{name} | Update Channel Details
*ChannelsApi* | [**v4_channels_post**](docs/ChannelsApi.md#v4_channels_post) | **POST** /v4/channels/ | Create a New Channel
*DKIMsApi* | [**v4_domains_domain_name_delete**](docs/DKIMsApi.md#v4_domains_domain_name_delete) | **DELETE** /v4/domains/{domain_name} | Delete Domain
*DKIMsApi* | [**v4_domains_domain_name_dkim_keys_delete**](docs/DKIMsApi.md#v4_domains_domain_name_dkim_keys_delete) | **DELETE** /v4/domains/{domain_name}/dkim_keys | Delete DKIM for Domain
*DKIMsApi* | [**v4_domains_domain_name_dkim_keys_get**](docs/DKIMsApi.md#v4_domains_domain_name_dkim_keys_get) | **GET** /v4/domains/{domain_name}/dkim_keys | Get DKIM for Domain
*DKIMsApi* | [**v4_domains_domain_name_dkim_keys_patch**](docs/DKIMsApi.md#v4_domains_domain_name_dkim_keys_patch) | **PATCH** /v4/domains/{domain_name}/dkim_keys | Update DKIM Key Details
*DKIMsApi* | [**v4_domains_domain_name_dkim_keys_post**](docs/DKIMsApi.md#v4_domains_domain_name_dkim_keys_post) | **POST** /v4/domains/{domain_name}/dkim_keys | Add DKIM for Domain
*DKIMsApi* | [**v4_domains_domain_name_get**](docs/DKIMsApi.md#v4_domains_domain_name_get) | **GET** /v4/domains/{domain_name} | Get Domain Details
*DKIMsApi* | [**v4_domains_domain_name_patch**](docs/DKIMsApi.md#v4_domains_domain_name_patch) | **PATCH** /v4/domains/{domain_name} | Update Domain Details
*DKIMsApi* | [**v4_domains_get**](docs/DKIMsApi.md#v4_domains_get) | **GET** /v4/domains/ | Get All Registered Domains
*DKIMsApi* | [**v4_domains_post**](docs/DKIMsApi.md#v4_domains_post) | **POST** /v4/domains/ | Register a Domain
*MessagesApi* | [**v4_messages_get**](docs/MessagesApi.md#v4_messages_get) | **GET** /v4/messages | Get Detailed Messages Info
*MessagesApi* | [**v4_messages_mime_post**](docs/MessagesApi.md#v4_messages_mime_post) | **POST** /v4/messages/mime | Send MIME Message
*MessagesApi* | [**v4_messages_post**](docs/MessagesApi.md#v4_messages_post) | **POST** /v4/messages | Send a Message
*ReportsApi* | [**v4_reports_get**](docs/ReportsApi.md#v4_reports_get) | **GET** /v4/reports/ | Get All Reports
*ReportsApi* | [**v4_reports_ondemand_post**](docs/ReportsApi.md#v4_reports_ondemand_post) | **POST** /v4/reports/ondemand | Create On-Demand Report
*ReportsApi* | [**v4_reports_periodic_post**](docs/ReportsApi.md#v4_reports_periodic_post) | **POST** /v4/reports/periodic | Create Periodic Report
*ReportsApi* | [**v4_reports_periodic_report_id_delete**](docs/ReportsApi.md#v4_reports_periodic_report_id_delete) | **DELETE** /v4/reports/periodic/{report_id} | Delete a Periodic Report
*ReportsApi* | [**v4_reports_periodic_report_id_patch**](docs/ReportsApi.md#v4_reports_periodic_report_id_patch) | **PATCH** /v4/reports/periodic/{report_id} | Update Periodic Report
*ReportsApi* | [**v4_reports_report_id_get**](docs/ReportsApi.md#v4_reports_report_id_get) | **GET** /v4/reports/{report_id} | Get Report Details
*StatisticsApi* | [**v4_stats_duration_slice_slice_specifier_group_by_get**](docs/StatisticsApi.md#v4_stats_duration_slice_slice_specifier_group_by_get) | **GET** /v4/stats/{duration}/{slice}/{slice_specifier}/{group_by} | Return event aggregates for the specified slices and duration. Slices can be chained.


## Documentation For Models

 - [APIKey](docs/APIKey.md)
 - [Account](docs/Account.md)
 - [AccountData](docs/AccountData.md)
 - [AccountDataAddress](docs/AccountDataAddress.md)
 - [BadRequestSchema](docs/BadRequestSchema.md)
 - [BadRequestSchemaData](docs/BadRequestSchemaData.md)
 - [Channel](docs/Channel.md)
 - [ChannelData](docs/ChannelData.md)
 - [Channels](docs/Channels.md)
 - [ChannelsData](docs/ChannelsData.md)
 - [ChannelsDataItems](docs/ChannelsDataItems.md)
 - [CreateCallbackResponse](docs/CreateCallbackResponse.md)
 - [CreateDkimKey](docs/CreateDkimKey.md)
 - [CreateDkimKeyData](docs/CreateDkimKeyData.md)
 - [CreateDomainResponse](docs/CreateDomainResponse.md)
 - [CreateDomainResponseData](docs/CreateDomainResponseData.md)
 - [DurationValue](docs/DurationValue.md)
 - [GetAlertDetails](docs/GetAlertDetails.md)
 - [GetAlertDetailsData](docs/GetAlertDetailsData.md)
 - [GetAlertResponse](docs/GetAlertResponse.md)
 - [GetAlertResponseData](docs/GetAlertResponseData.md)
 - [GetAlertResponseDataItems](docs/GetAlertResponseDataItems.md)
 - [GetApiKeys](docs/GetApiKeys.md)
 - [GetApiKeysData](docs/GetApiKeysData.md)
 - [GetApiKeysDataItems](docs/GetApiKeysDataItems.md)
 - [GetCallbackDetails](docs/GetCallbackDetails.md)
 - [GetCallbackDetailsData](docs/GetCallbackDetailsData.md)
 - [GetCallbackLogs](docs/GetCallbackLogs.md)
 - [GetCallbackLogsData](docs/GetCallbackLogsData.md)
 - [GetCallbackLogsDataItems](docs/GetCallbackLogsDataItems.md)
 - [GetCallbackResponse](docs/GetCallbackResponse.md)
 - [GetCallbackResponseData](docs/GetCallbackResponseData.md)
 - [GetCallbackResponseDataItems](docs/GetCallbackResponseDataItems.md)
 - [GetDomainDetails](docs/GetDomainDetails.md)
 - [GetDomainDetailsData](docs/GetDomainDetailsData.md)
 - [GetDomainDetailsResponse](docs/GetDomainDetailsResponse.md)
 - [GetDomainDetailsResponseData](docs/GetDomainDetailsResponseData.md)
 - [GetDomainsResponse](docs/GetDomainsResponse.md)
 - [GetDomainsResponseData](docs/GetDomainsResponseData.md)
 - [GetDomainsResponseDataItems](docs/GetDomainsResponseDataItems.md)
 - [InlineObject](docs/InlineObject.md)
 - [InlineObject1](docs/InlineObject1.md)
 - [InvalidKey](docs/InvalidKey.md)
 - [InvalidKeyData](docs/InvalidKeyData.md)
 - [InvalidKeyDataErrors](docs/InvalidKeyDataErrors.md)
 - [MessagesResponse](docs/MessagesResponse.md)
 - [MessagesResponseData](docs/MessagesResponseData.md)
 - [MessagesResponseDataAbuse](docs/MessagesResponseDataAbuse.md)
 - [MessagesResponseDataAbuseComplaints](docs/MessagesResponseDataAbuseComplaints.md)
 - [MessagesResponseDataClicks](docs/MessagesResponseDataClicks.md)
 - [MessagesResponseDataClicksItems](docs/MessagesResponseDataClicksItems.md)
 - [MessagesResponseDataDetails](docs/MessagesResponseDataDetails.md)
 - [MessagesResponseDataDetailsDelivery](docs/MessagesResponseDataDetailsDelivery.md)
 - [MessagesResponseDataItems](docs/MessagesResponseDataItems.md)
 - [MessagesResponseDataMsgData](docs/MessagesResponseDataMsgData.md)
 - [MessagesResponseDataOpens](docs/MessagesResponseDataOpens.md)
 - [MessagesResponseDataOpensItems](docs/MessagesResponseDataOpensItems.md)
 - [MessagesResponseDataUnsubs](docs/MessagesResponseDataUnsubs.md)
 - [MessagesResponseDataUnsubsItems](docs/MessagesResponseDataUnsubsItems.md)
 - [MimeResponse](docs/MimeResponse.md)
 - [PostMessageResponse](docs/PostMessageResponse.md)
 - [PostMessageResponseData](docs/PostMessageResponseData.md)
 - [Report](docs/Report.md)
 - [Reports](docs/Reports.md)
 - [ReportsData](docs/ReportsData.md)
 - [ReportsDataOndemand](docs/ReportsDataOndemand.md)
 - [ReportsDataPeriodic](docs/ReportsDataPeriodic.md)
 - [SliceValue](docs/SliceValue.md)
 - [StatsResponse](docs/StatsResponse.md)
 - [StatsResponseData](docs/StatsResponseData.md)
 - [StatsResponseDataItems](docs/StatsResponseDataItems.md)
 - [StatusResponse](docs/StatusResponse.md)
 - [UpdateAccountResponse](docs/UpdateAccountResponse.md)
 - [UpdateAccountResponseData](docs/UpdateAccountResponseData.md)
 - [V4MessagesBody](docs/V4MessagesBody.md)
 - [V4MessagesBodyAttachments](docs/V4MessagesBodyAttachments.md)
 - [V4MessagesBodyParts](docs/V4MessagesBodyParts.md)
 - [V4MessagesMimeRecipients](docs/V4MessagesMimeRecipients.md)
 - [V4MessagesOriginator](docs/V4MessagesOriginator.md)
 - [V4MessagesRecipients](docs/V4MessagesRecipients.md)
 - [V4MessagesRecipientsTo](docs/V4MessagesRecipientsTo.md)


## Documentation For Authorization


## apiID

- **Type**: API key
- **API key parameter name**: api_key
- **Location**: URL query string


## apiKey

- **Type**: API key
- **API key parameter name**: X-SMTPCOM-API
- **Location**: HTTP header


## basicAuth

- **Type**: HTTP basic authentication


## Author

support@smtp.com


