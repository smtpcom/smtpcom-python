# smtp.ReportsApi

All URIs are relative to *https://api.smtp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v4_reports_get**](ReportsApi.md#v4_reports_get) | **GET** /v4/reports/ | Get All Reports
[**v4_reports_ondemand_post**](ReportsApi.md#v4_reports_ondemand_post) | **POST** /v4/reports/ondemand | Create On-Demand Report
[**v4_reports_periodic_post**](ReportsApi.md#v4_reports_periodic_post) | **POST** /v4/reports/periodic | Create Periodic Report
[**v4_reports_periodic_report_id_delete**](ReportsApi.md#v4_reports_periodic_report_id_delete) | **DELETE** /v4/reports/periodic/{report_id} | Delete a Periodic Report
[**v4_reports_periodic_report_id_patch**](ReportsApi.md#v4_reports_periodic_report_id_patch) | **PATCH** /v4/reports/periodic/{report_id} | Update Periodic Report
[**v4_reports_report_id_get**](ReportsApi.md#v4_reports_report_id_get) | **GET** /v4/reports/{report_id} | Get Report Details


# **v4_reports_get**
> Reports v4_reports_get()

Get All Reports

### Example

* Api Key Authentication (apiID):
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
    api_instance = smtpcom.ReportsApi(api_client)
    
    try:
        # Get All Reports
        api_response = api_instance.v4_reports_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportsApi->v4_reports_get: %s\n" % e)
```

* Api Key Authentication (apiKey):
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
    api_instance = smtpcom.ReportsApi(api_client)
    
    try:
        # Get All Reports
        api_response = api_instance.v4_reports_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportsApi->v4_reports_get: %s\n" % e)
```

* Basic Authentication (basicAuth):
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
    api_instance = smtpcom.ReportsApi(api_client)
    
    try:
        # Get All Reports
        api_response = api_instance.v4_reports_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportsApi->v4_reports_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Reports**](Reports.md)

### Authorization

[apiID](../README.md#apiID), [apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get All Reports |  -  |
**400** | Query or path params invalid |  -  |
**401** | Invalid API Key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_reports_ondemand_post**
> StatusResponse v4_reports_ondemand_post(start, channel=channel, type=type, end=end, domain=domain, rcpt_domain=rcpt_domain, events=events, columns=columns)

Create On-Demand Report

### Example

* Api Key Authentication (apiID):
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
    api_instance = smtpcom.ReportsApi(api_client)
    start = 56 # int | Start date/time of the report in RFC 2822 or UNIX epoch format
channel = 'channel_example' # str | Name of the channel for which a given report has been defined (optional)
type = 'type_example' # str | Type or report format. If not specified defaults to “csv” - currently the only supported type (optional)
end = 'end_example' # str | End date/time of the report in RFC 2822 or UNIX epoch format (default - now) (optional)
domain = 'domain_example' # str | Filter by the “from” domain of emails (optional)
rcpt_domain = 'rcpt_domain_example' # str | Filter by the “to” domain of emails (optional)
events = 'events_example' # str | Filter by event type. Valid event are:  * hard_bounced - just hard bounces * failed - all failed messages, i.e. hard_bounced + the rest of failed * delivered - delivered messages * sent - delivered+failed (default events value) * pending - pending messages * total - all messages, i.e. sent+pending * abuse - spam complaints  (optional)
columns = 'columns_example' # str | Array of columns to be specified in the report. These can differ based on any specified event type filter.   Possible column values for all reports are: * `message_id` - Unique message ID * from - From Address * to - Recipient Address * time_rcv - Date Received in RFC 2822 or UNIX epoch format * time_snt - Date Delivered in RFC 2822 or UNIX epoch format * channel - Name of a channel  Additional column values for message reports (hard_bounced, failed, delivered, total) include: * status - Status of delivery * code - SMTP Response Code * message - SMTP Response message * tries - Amount of re-tries (deferred states before final)  Additional column values for spam reports include:  * report_time - Date when an abuse complaint has been reported, RFC 2822 or UNIX epoch format * subject - Email Subject  Additional column values for pending reports include:  * status - Current email status  If not specified all relevant columns are included.  (optional)

    try:
        # Create On-Demand Report
        api_response = api_instance.v4_reports_ondemand_post(start, channel=channel, type=type, end=end, domain=domain, rcpt_domain=rcpt_domain, events=events, columns=columns)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportsApi->v4_reports_ondemand_post: %s\n" % e)
```

* Api Key Authentication (apiKey):
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
    api_instance = smtpcom.ReportsApi(api_client)
    start = 56 # int | Start date/time of the report in RFC 2822 or UNIX epoch format
channel = 'channel_example' # str | Name of the channel for which a given report has been defined (optional)
type = 'type_example' # str | Type or report format. If not specified defaults to “csv” - currently the only supported type (optional)
end = 'end_example' # str | End date/time of the report in RFC 2822 or UNIX epoch format (default - now) (optional)
domain = 'domain_example' # str | Filter by the “from” domain of emails (optional)
rcpt_domain = 'rcpt_domain_example' # str | Filter by the “to” domain of emails (optional)
events = 'events_example' # str | Filter by event type. Valid event are:  * hard_bounced - just hard bounces * failed - all failed messages, i.e. hard_bounced + the rest of failed * delivered - delivered messages * sent - delivered+failed (default events value) * pending - pending messages * total - all messages, i.e. sent+pending * abuse - spam complaints  (optional)
columns = 'columns_example' # str | Array of columns to be specified in the report. These can differ based on any specified event type filter.   Possible column values for all reports are: * `message_id` - Unique message ID * from - From Address * to - Recipient Address * time_rcv - Date Received in RFC 2822 or UNIX epoch format * time_snt - Date Delivered in RFC 2822 or UNIX epoch format * channel - Name of a channel  Additional column values for message reports (hard_bounced, failed, delivered, total) include: * status - Status of delivery * code - SMTP Response Code * message - SMTP Response message * tries - Amount of re-tries (deferred states before final)  Additional column values for spam reports include:  * report_time - Date when an abuse complaint has been reported, RFC 2822 or UNIX epoch format * subject - Email Subject  Additional column values for pending reports include:  * status - Current email status  If not specified all relevant columns are included.  (optional)

    try:
        # Create On-Demand Report
        api_response = api_instance.v4_reports_ondemand_post(start, channel=channel, type=type, end=end, domain=domain, rcpt_domain=rcpt_domain, events=events, columns=columns)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportsApi->v4_reports_ondemand_post: %s\n" % e)
```

* Basic Authentication (basicAuth):
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
    api_instance = smtpcom.ReportsApi(api_client)
    start = 56 # int | Start date/time of the report in RFC 2822 or UNIX epoch format
channel = 'channel_example' # str | Name of the channel for which a given report has been defined (optional)
type = 'type_example' # str | Type or report format. If not specified defaults to “csv” - currently the only supported type (optional)
end = 'end_example' # str | End date/time of the report in RFC 2822 or UNIX epoch format (default - now) (optional)
domain = 'domain_example' # str | Filter by the “from” domain of emails (optional)
rcpt_domain = 'rcpt_domain_example' # str | Filter by the “to” domain of emails (optional)
events = 'events_example' # str | Filter by event type. Valid event are:  * hard_bounced - just hard bounces * failed - all failed messages, i.e. hard_bounced + the rest of failed * delivered - delivered messages * sent - delivered+failed (default events value) * pending - pending messages * total - all messages, i.e. sent+pending * abuse - spam complaints  (optional)
columns = 'columns_example' # str | Array of columns to be specified in the report. These can differ based on any specified event type filter.   Possible column values for all reports are: * `message_id` - Unique message ID * from - From Address * to - Recipient Address * time_rcv - Date Received in RFC 2822 or UNIX epoch format * time_snt - Date Delivered in RFC 2822 or UNIX epoch format * channel - Name of a channel  Additional column values for message reports (hard_bounced, failed, delivered, total) include: * status - Status of delivery * code - SMTP Response Code * message - SMTP Response message * tries - Amount of re-tries (deferred states before final)  Additional column values for spam reports include:  * report_time - Date when an abuse complaint has been reported, RFC 2822 or UNIX epoch format * subject - Email Subject  Additional column values for pending reports include:  * status - Current email status  If not specified all relevant columns are included.  (optional)

    try:
        # Create On-Demand Report
        api_response = api_instance.v4_reports_ondemand_post(start, channel=channel, type=type, end=end, domain=domain, rcpt_domain=rcpt_domain, events=events, columns=columns)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportsApi->v4_reports_ondemand_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| Start date/time of the report in RFC 2822 or UNIX epoch format | 
 **channel** | **str**| Name of the channel for which a given report has been defined | [optional] 
 **type** | **str**| Type or report format. If not specified defaults to “csv” - currently the only supported type | [optional] 
 **end** | **str**| End date/time of the report in RFC 2822 or UNIX epoch format (default - now) | [optional] 
 **domain** | **str**| Filter by the “from” domain of emails | [optional] 
 **rcpt_domain** | **str**| Filter by the “to” domain of emails | [optional] 
 **events** | **str**| Filter by event type. Valid event are:  * hard_bounced - just hard bounces * failed - all failed messages, i.e. hard_bounced + the rest of failed * delivered - delivered messages * sent - delivered+failed (default events value) * pending - pending messages * total - all messages, i.e. sent+pending * abuse - spam complaints  | [optional] 
 **columns** | **str**| Array of columns to be specified in the report. These can differ based on any specified event type filter.   Possible column values for all reports are: * &#x60;message_id&#x60; - Unique message ID * from - From Address * to - Recipient Address * time_rcv - Date Received in RFC 2822 or UNIX epoch format * time_snt - Date Delivered in RFC 2822 or UNIX epoch format * channel - Name of a channel  Additional column values for message reports (hard_bounced, failed, delivered, total) include: * status - Status of delivery * code - SMTP Response Code * message - SMTP Response message * tries - Amount of re-tries (deferred states before final)  Additional column values for spam reports include:  * report_time - Date when an abuse complaint has been reported, RFC 2822 or UNIX epoch format * subject - Email Subject  Additional column values for pending reports include:  * status - Current email status  If not specified all relevant columns are included.  | [optional] 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[apiID](../README.md#apiID), [apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Create On-Demand Report |  -  |
**400** | Query or path params invalid |  -  |
**401** | Invalid API Key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_reports_periodic_post**
> StatusResponse v4_reports_periodic_post(frequency, report_time, channel=channel, notify_method=notify_method, notify_dest=notify_dest, domain=domain, rcpt_domain=rcpt_domain, events=events, columns=columns)

Create Periodic Report

### Example

* Api Key Authentication (apiID):
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
    api_instance = smtpcom.ReportsApi(api_client)
    frequency = 'frequency_example' # str | Report frequency – one of:   * daily - every day at a specified hour   * weekly  - Mondays at a specified hour   * monthly - 1st day of the month at a specified hour 
report_time = 56 # int | The hour at which the report should be sent. Value values range from 0 to 23
channel = 'channel_example' # str | Name of the channel for which a given report has been defined (optional)
notify_method = 'notify_method_example' # str | Notification method to be used when report is completed and can be downloaded (optional)
notify_dest = 'notify_dest_example' # str | A valid URL which will accept the report completion notification. The payload will be ```   {\"message\": \"success\", \"id\": string} ``` where `id` is a Unique report ID  (optional)
domain = 'domain_example' # str | Filter by the “From” domain of emails (optional)
rcpt_domain = 'rcpt_domain_example' # str | Filter by the “To” domain of emails (optional)
events = 'events_example' # str | Filter by event type. Valid event are:  * hard_bounced - just hard bounces * failed - all failed messages, i.e. hard_bounced + the rest of failed * delivered - delivered messages * sent - delivered+failed (default events value) * pending - pending messages * total - all messages, i.e. sent+pending * abuse - spam complaints  (optional)
columns = 'columns_example' # str | Array of columns to be specified in the report. These can differ based on any specified event type filter.   Possible column values are: * `message_id` - Unique message ID * from - From Address * to - Recipient Address * time_rcv - Date Received in RFC 2822 or UNIX epoch format * time_snt - Date Delivered in RFC 2822 or UNIX epoch format * channel - Name of a channel  Additional column values for message reports (hard_bounced, failed, delivered, total) include: * status - Status of delivery * code - SMTP Response Code * message - SMTP Response message * tries - Amount of re-tries (deferred states before final)  Additional column values for spam reports include:  * report_time - Date when an abuse complaint has been reported, RFC 2822 or UNIX epoch format * subject - Email Subject  Additional column values for pending reports include:  * status - Current email status  If not specified all relevant columns are included.  (optional)

    try:
        # Create Periodic Report
        api_response = api_instance.v4_reports_periodic_post(frequency, report_time, channel=channel, notify_method=notify_method, notify_dest=notify_dest, domain=domain, rcpt_domain=rcpt_domain, events=events, columns=columns)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportsApi->v4_reports_periodic_post: %s\n" % e)
```

* Api Key Authentication (apiKey):
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
    api_instance = smtpcom.ReportsApi(api_client)
    frequency = 'frequency_example' # str | Report frequency – one of:   * daily - every day at a specified hour   * weekly  - Mondays at a specified hour   * monthly - 1st day of the month at a specified hour 
report_time = 56 # int | The hour at which the report should be sent. Value values range from 0 to 23
channel = 'channel_example' # str | Name of the channel for which a given report has been defined (optional)
notify_method = 'notify_method_example' # str | Notification method to be used when report is completed and can be downloaded (optional)
notify_dest = 'notify_dest_example' # str | A valid URL which will accept the report completion notification. The payload will be ```   {\"message\": \"success\", \"id\": string} ``` where `id` is a Unique report ID  (optional)
domain = 'domain_example' # str | Filter by the “From” domain of emails (optional)
rcpt_domain = 'rcpt_domain_example' # str | Filter by the “To” domain of emails (optional)
events = 'events_example' # str | Filter by event type. Valid event are:  * hard_bounced - just hard bounces * failed - all failed messages, i.e. hard_bounced + the rest of failed * delivered - delivered messages * sent - delivered+failed (default events value) * pending - pending messages * total - all messages, i.e. sent+pending * abuse - spam complaints  (optional)
columns = 'columns_example' # str | Array of columns to be specified in the report. These can differ based on any specified event type filter.   Possible column values are: * `message_id` - Unique message ID * from - From Address * to - Recipient Address * time_rcv - Date Received in RFC 2822 or UNIX epoch format * time_snt - Date Delivered in RFC 2822 or UNIX epoch format * channel - Name of a channel  Additional column values for message reports (hard_bounced, failed, delivered, total) include: * status - Status of delivery * code - SMTP Response Code * message - SMTP Response message * tries - Amount of re-tries (deferred states before final)  Additional column values for spam reports include:  * report_time - Date when an abuse complaint has been reported, RFC 2822 or UNIX epoch format * subject - Email Subject  Additional column values for pending reports include:  * status - Current email status  If not specified all relevant columns are included.  (optional)

    try:
        # Create Periodic Report
        api_response = api_instance.v4_reports_periodic_post(frequency, report_time, channel=channel, notify_method=notify_method, notify_dest=notify_dest, domain=domain, rcpt_domain=rcpt_domain, events=events, columns=columns)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportsApi->v4_reports_periodic_post: %s\n" % e)
```

* Basic Authentication (basicAuth):
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
    api_instance = smtpcom.ReportsApi(api_client)
    frequency = 'frequency_example' # str | Report frequency – one of:   * daily - every day at a specified hour   * weekly  - Mondays at a specified hour   * monthly - 1st day of the month at a specified hour 
report_time = 56 # int | The hour at which the report should be sent. Value values range from 0 to 23
channel = 'channel_example' # str | Name of the channel for which a given report has been defined (optional)
notify_method = 'notify_method_example' # str | Notification method to be used when report is completed and can be downloaded (optional)
notify_dest = 'notify_dest_example' # str | A valid URL which will accept the report completion notification. The payload will be ```   {\"message\": \"success\", \"id\": string} ``` where `id` is a Unique report ID  (optional)
domain = 'domain_example' # str | Filter by the “From” domain of emails (optional)
rcpt_domain = 'rcpt_domain_example' # str | Filter by the “To” domain of emails (optional)
events = 'events_example' # str | Filter by event type. Valid event are:  * hard_bounced - just hard bounces * failed - all failed messages, i.e. hard_bounced + the rest of failed * delivered - delivered messages * sent - delivered+failed (default events value) * pending - pending messages * total - all messages, i.e. sent+pending * abuse - spam complaints  (optional)
columns = 'columns_example' # str | Array of columns to be specified in the report. These can differ based on any specified event type filter.   Possible column values are: * `message_id` - Unique message ID * from - From Address * to - Recipient Address * time_rcv - Date Received in RFC 2822 or UNIX epoch format * time_snt - Date Delivered in RFC 2822 or UNIX epoch format * channel - Name of a channel  Additional column values for message reports (hard_bounced, failed, delivered, total) include: * status - Status of delivery * code - SMTP Response Code * message - SMTP Response message * tries - Amount of re-tries (deferred states before final)  Additional column values for spam reports include:  * report_time - Date when an abuse complaint has been reported, RFC 2822 or UNIX epoch format * subject - Email Subject  Additional column values for pending reports include:  * status - Current email status  If not specified all relevant columns are included.  (optional)

    try:
        # Create Periodic Report
        api_response = api_instance.v4_reports_periodic_post(frequency, report_time, channel=channel, notify_method=notify_method, notify_dest=notify_dest, domain=domain, rcpt_domain=rcpt_domain, events=events, columns=columns)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportsApi->v4_reports_periodic_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **frequency** | **str**| Report frequency – one of:   * daily - every day at a specified hour   * weekly  - Mondays at a specified hour   * monthly - 1st day of the month at a specified hour  | 
 **report_time** | **int**| The hour at which the report should be sent. Value values range from 0 to 23 | 
 **channel** | **str**| Name of the channel for which a given report has been defined | [optional] 
 **notify_method** | **str**| Notification method to be used when report is completed and can be downloaded | [optional] 
 **notify_dest** | **str**| A valid URL which will accept the report completion notification. The payload will be &#x60;&#x60;&#x60;   {\&quot;message\&quot;: \&quot;success\&quot;, \&quot;id\&quot;: string} &#x60;&#x60;&#x60; where &#x60;id&#x60; is a Unique report ID  | [optional] 
 **domain** | **str**| Filter by the “From” domain of emails | [optional] 
 **rcpt_domain** | **str**| Filter by the “To” domain of emails | [optional] 
 **events** | **str**| Filter by event type. Valid event are:  * hard_bounced - just hard bounces * failed - all failed messages, i.e. hard_bounced + the rest of failed * delivered - delivered messages * sent - delivered+failed (default events value) * pending - pending messages * total - all messages, i.e. sent+pending * abuse - spam complaints  | [optional] 
 **columns** | **str**| Array of columns to be specified in the report. These can differ based on any specified event type filter.   Possible column values are: * &#x60;message_id&#x60; - Unique message ID * from - From Address * to - Recipient Address * time_rcv - Date Received in RFC 2822 or UNIX epoch format * time_snt - Date Delivered in RFC 2822 or UNIX epoch format * channel - Name of a channel  Additional column values for message reports (hard_bounced, failed, delivered, total) include: * status - Status of delivery * code - SMTP Response Code * message - SMTP Response message * tries - Amount of re-tries (deferred states before final)  Additional column values for spam reports include:  * report_time - Date when an abuse complaint has been reported, RFC 2822 or UNIX epoch format * subject - Email Subject  Additional column values for pending reports include:  * status - Current email status  If not specified all relevant columns are included.  | [optional] 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[apiID](../README.md#apiID), [apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Create Report |  -  |
**400** | Query or path params invalid |  -  |
**401** | Invalid API Key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_reports_periodic_report_id_delete**
> StatusResponse v4_reports_periodic_report_id_delete(report_id)

Delete a Periodic Report

### Example

* Api Key Authentication (apiID):
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
    api_instance = smtpcom.ReportsApi(api_client)
    report_id = 'report_id_example' # str | Id of a given report

    try:
        # Delete a Periodic Report
        api_response = api_instance.v4_reports_periodic_report_id_delete(report_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportsApi->v4_reports_periodic_report_id_delete: %s\n" % e)
```

* Api Key Authentication (apiKey):
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
    api_instance = smtpcom.ReportsApi(api_client)
    report_id = 'report_id_example' # str | Id of a given report

    try:
        # Delete a Periodic Report
        api_response = api_instance.v4_reports_periodic_report_id_delete(report_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportsApi->v4_reports_periodic_report_id_delete: %s\n" % e)
```

* Basic Authentication (basicAuth):
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
    api_instance = smtpcom.ReportsApi(api_client)
    report_id = 'report_id_example' # str | Id of a given report

    try:
        # Delete a Periodic Report
        api_response = api_instance.v4_reports_periodic_report_id_delete(report_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportsApi->v4_reports_periodic_report_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| Id of a given report | 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[apiID](../README.md#apiID), [apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete a Periodic Report |  -  |
**400** | Query or path params invalid |  -  |
**401** | Invalid API Key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_reports_periodic_report_id_patch**
> StatusResponse v4_reports_periodic_report_id_patch(report_id, frequency, report_time, channel=channel, events=events)

Update Periodic Report

### Example

* Api Key Authentication (apiID):
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
    api_instance = smtpcom.ReportsApi(api_client)
    report_id = 'report_id_example' # str | Id of the report to be updated
frequency = 'frequency_example' # str | Report frequency – one of:  * daily - every day at a specified hour  * weekly  - Mondays at a specified hour  * monthly - first day of the month at a specified hour. 
report_time = 56 # int | The hour at which the report should be sent. Value values range from 0 to 23
channel = 'channel_example' # str | Name of channel (sender). If not specified all channels will be reported (optional)
events = 'events_example' # str | Filter by event type. Valid event are: * hard_bounced - just hard bounces * failed - all failed messages, i.e. hard_bounced + the rest of failed * delivered - delivered messages * sent - delivered+failed (default events value) * pending - pending messages * total - all messages, i.e. sent+pending * abuse - spam complaints  If not specified all events are included.  (optional)

    try:
        # Update Periodic Report
        api_response = api_instance.v4_reports_periodic_report_id_patch(report_id, frequency, report_time, channel=channel, events=events)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportsApi->v4_reports_periodic_report_id_patch: %s\n" % e)
```

* Api Key Authentication (apiKey):
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
    api_instance = smtpcom.ReportsApi(api_client)
    report_id = 'report_id_example' # str | Id of the report to be updated
frequency = 'frequency_example' # str | Report frequency – one of:  * daily - every day at a specified hour  * weekly  - Mondays at a specified hour  * monthly - first day of the month at a specified hour. 
report_time = 56 # int | The hour at which the report should be sent. Value values range from 0 to 23
channel = 'channel_example' # str | Name of channel (sender). If not specified all channels will be reported (optional)
events = 'events_example' # str | Filter by event type. Valid event are: * hard_bounced - just hard bounces * failed - all failed messages, i.e. hard_bounced + the rest of failed * delivered - delivered messages * sent - delivered+failed (default events value) * pending - pending messages * total - all messages, i.e. sent+pending * abuse - spam complaints  If not specified all events are included.  (optional)

    try:
        # Update Periodic Report
        api_response = api_instance.v4_reports_periodic_report_id_patch(report_id, frequency, report_time, channel=channel, events=events)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportsApi->v4_reports_periodic_report_id_patch: %s\n" % e)
```

* Basic Authentication (basicAuth):
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
    api_instance = smtpcom.ReportsApi(api_client)
    report_id = 'report_id_example' # str | Id of the report to be updated
frequency = 'frequency_example' # str | Report frequency – one of:  * daily - every day at a specified hour  * weekly  - Mondays at a specified hour  * monthly - first day of the month at a specified hour. 
report_time = 56 # int | The hour at which the report should be sent. Value values range from 0 to 23
channel = 'channel_example' # str | Name of channel (sender). If not specified all channels will be reported (optional)
events = 'events_example' # str | Filter by event type. Valid event are: * hard_bounced - just hard bounces * failed - all failed messages, i.e. hard_bounced + the rest of failed * delivered - delivered messages * sent - delivered+failed (default events value) * pending - pending messages * total - all messages, i.e. sent+pending * abuse - spam complaints  If not specified all events are included.  (optional)

    try:
        # Update Periodic Report
        api_response = api_instance.v4_reports_periodic_report_id_patch(report_id, frequency, report_time, channel=channel, events=events)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportsApi->v4_reports_periodic_report_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| Id of the report to be updated | 
 **frequency** | **str**| Report frequency – one of:  * daily - every day at a specified hour  * weekly  - Mondays at a specified hour  * monthly - first day of the month at a specified hour.  | 
 **report_time** | **int**| The hour at which the report should be sent. Value values range from 0 to 23 | 
 **channel** | **str**| Name of channel (sender). If not specified all channels will be reported | [optional] 
 **events** | **str**| Filter by event type. Valid event are: * hard_bounced - just hard bounces * failed - all failed messages, i.e. hard_bounced + the rest of failed * delivered - delivered messages * sent - delivered+failed (default events value) * pending - pending messages * total - all messages, i.e. sent+pending * abuse - spam complaints  If not specified all events are included.  | [optional] 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[apiID](../README.md#apiID), [apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update Periodic Report |  -  |
**400** | Query or path params invalid |  -  |
**401** | Invalid API Key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_reports_report_id_get**
> Report v4_reports_report_id_get(report_id)

Get Report Details

### Example

* Api Key Authentication (apiID):
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
    api_instance = smtpcom.ReportsApi(api_client)
    report_id = 'report_id_example' # str | ID of a given report

    try:
        # Get Report Details
        api_response = api_instance.v4_reports_report_id_get(report_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportsApi->v4_reports_report_id_get: %s\n" % e)
```

* Api Key Authentication (apiKey):
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
    api_instance = smtpcom.ReportsApi(api_client)
    report_id = 'report_id_example' # str | ID of a given report

    try:
        # Get Report Details
        api_response = api_instance.v4_reports_report_id_get(report_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportsApi->v4_reports_report_id_get: %s\n" % e)
```

* Basic Authentication (basicAuth):
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
    api_instance = smtpcom.ReportsApi(api_client)
    report_id = 'report_id_example' # str | ID of a given report

    try:
        # Get Report Details
        api_response = api_instance.v4_reports_report_id_get(report_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportsApi->v4_reports_report_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| ID of a given report | 

### Return type

[**Report**](Report.md)

### Authorization

[apiID](../README.md#apiID), [apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Report Details |  -  |
**400** | Query or path params invalid |  -  |
**401** | Invalid API Key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

