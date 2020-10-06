# smtp.CallbacksApi

All URIs are relative to *https://api.smtp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v4_callbacks_delete**](CallbacksApi.md#v4_callbacks_delete) | **DELETE** /v4/callbacks/ | Delete All Callbacks
[**v4_callbacks_event_delete**](CallbacksApi.md#v4_callbacks_event_delete) | **DELETE** /v4/callbacks/{event} | Delete Callback
[**v4_callbacks_event_get**](CallbacksApi.md#v4_callbacks_event_get) | **GET** /v4/callbacks/{event} | Get Callback Details
[**v4_callbacks_event_patch**](CallbacksApi.md#v4_callbacks_event_patch) | **PATCH** /v4/callbacks/{event} | Update Callback Details
[**v4_callbacks_event_post**](CallbacksApi.md#v4_callbacks_event_post) | **POST** /v4/callbacks/{event} | Create Callback
[**v4_callbacks_get**](CallbacksApi.md#v4_callbacks_get) | **GET** /v4/callbacks/ | List All Callbacks
[**v4_callbacks_log_get**](CallbacksApi.md#v4_callbacks_log_get) | **GET** /v4/callbacks/log | View Callback Logs


# **v4_callbacks_delete**
> StatusResponse v4_callbacks_delete()

Delete All Callbacks

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
    api_instance = smtpcom.CallbacksApi(api_client)
    
    try:
        # Delete All Callbacks
        api_response = api_instance.v4_callbacks_delete()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CallbacksApi->v4_callbacks_delete: %s\n" % e)
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
    api_instance = smtpcom.CallbacksApi(api_client)
    
    try:
        # Delete All Callbacks
        api_response = api_instance.v4_callbacks_delete()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CallbacksApi->v4_callbacks_delete: %s\n" % e)
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
    api_instance = smtpcom.CallbacksApi(api_client)
    
    try:
        # Delete All Callbacks
        api_response = api_instance.v4_callbacks_delete()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CallbacksApi->v4_callbacks_delete: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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
**200** | Delete All Callbacks |  -  |
**400** | Query or path params invalid |  -  |
**401** | Invalid API Key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_callbacks_event_delete**
> StatusResponse v4_callbacks_event_delete(event, channel)

Delete Callback

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
    api_instance = smtpcom.CallbacksApi(api_client)
    event = 'event_example' # str | Event for which the callback has been created. Valid types are:  * delivered -  message delivered * failed - message bounced * complained - complaint received * bounceback - bounce back notification received * received - message received by our system * queued - message in queue (transient) * hard_bounced - hard bounce received * opened - message opened * clicked - URL in message clicked * unsubscribed - unsubscribe received 
channel = 'channel_example' # str | Name of the channel for which the callback has been created

    try:
        # Delete Callback
        api_response = api_instance.v4_callbacks_event_delete(event, channel)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CallbacksApi->v4_callbacks_event_delete: %s\n" % e)
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
    api_instance = smtpcom.CallbacksApi(api_client)
    event = 'event_example' # str | Event for which the callback has been created. Valid types are:  * delivered -  message delivered * failed - message bounced * complained - complaint received * bounceback - bounce back notification received * received - message received by our system * queued - message in queue (transient) * hard_bounced - hard bounce received * opened - message opened * clicked - URL in message clicked * unsubscribed - unsubscribe received 
channel = 'channel_example' # str | Name of the channel for which the callback has been created

    try:
        # Delete Callback
        api_response = api_instance.v4_callbacks_event_delete(event, channel)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CallbacksApi->v4_callbacks_event_delete: %s\n" % e)
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
    api_instance = smtpcom.CallbacksApi(api_client)
    event = 'event_example' # str | Event for which the callback has been created. Valid types are:  * delivered -  message delivered * failed - message bounced * complained - complaint received * bounceback - bounce back notification received * received - message received by our system * queued - message in queue (transient) * hard_bounced - hard bounce received * opened - message opened * clicked - URL in message clicked * unsubscribed - unsubscribe received 
channel = 'channel_example' # str | Name of the channel for which the callback has been created

    try:
        # Delete Callback
        api_response = api_instance.v4_callbacks_event_delete(event, channel)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CallbacksApi->v4_callbacks_event_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event** | **str**| Event for which the callback has been created. Valid types are:  * delivered -  message delivered * failed - message bounced * complained - complaint received * bounceback - bounce back notification received * received - message received by our system * queued - message in queue (transient) * hard_bounced - hard bounce received * opened - message opened * clicked - URL in message clicked * unsubscribed - unsubscribe received  | 
 **channel** | **str**| Name of the channel for which the callback has been created | 

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
**200** | Delete Callback |  -  |
**400** | Query or path params invalid |  -  |
**401** | Invalid API Key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_callbacks_event_get**
> GetCallbackDetails v4_callbacks_event_get(event, channel)

Get Callback Details

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
    api_instance = smtpcom.CallbacksApi(api_client)
    event = 'event_example' # str | Event for which the callback has been created. Valid types are:  * delivered -  message delivered * failed - message bounced * complained - complaint received * bounceback - bounce back notification received * received - message received by our system * queued - message in queue (transient) * hard_bounced - hard bounce received * opened - message opened * clicked - URL in message clicked * unsubscribed - unsubscribe received 
channel = 'channel_example' # str | Name of the channel for which the callback has been created

    try:
        # Get Callback Details
        api_response = api_instance.v4_callbacks_event_get(event, channel)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CallbacksApi->v4_callbacks_event_get: %s\n" % e)
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
    api_instance = smtpcom.CallbacksApi(api_client)
    event = 'event_example' # str | Event for which the callback has been created. Valid types are:  * delivered -  message delivered * failed - message bounced * complained - complaint received * bounceback - bounce back notification received * received - message received by our system * queued - message in queue (transient) * hard_bounced - hard bounce received * opened - message opened * clicked - URL in message clicked * unsubscribed - unsubscribe received 
channel = 'channel_example' # str | Name of the channel for which the callback has been created

    try:
        # Get Callback Details
        api_response = api_instance.v4_callbacks_event_get(event, channel)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CallbacksApi->v4_callbacks_event_get: %s\n" % e)
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
    api_instance = smtpcom.CallbacksApi(api_client)
    event = 'event_example' # str | Event for which the callback has been created. Valid types are:  * delivered -  message delivered * failed - message bounced * complained - complaint received * bounceback - bounce back notification received * received - message received by our system * queued - message in queue (transient) * hard_bounced - hard bounce received * opened - message opened * clicked - URL in message clicked * unsubscribed - unsubscribe received 
channel = 'channel_example' # str | Name of the channel for which the callback has been created

    try:
        # Get Callback Details
        api_response = api_instance.v4_callbacks_event_get(event, channel)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CallbacksApi->v4_callbacks_event_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event** | **str**| Event for which the callback has been created. Valid types are:  * delivered -  message delivered * failed - message bounced * complained - complaint received * bounceback - bounce back notification received * received - message received by our system * queued - message in queue (transient) * hard_bounced - hard bounce received * opened - message opened * clicked - URL in message clicked * unsubscribed - unsubscribe received  | 
 **channel** | **str**| Name of the channel for which the callback has been created | 

### Return type

[**GetCallbackDetails**](GetCallbackDetails.md)

### Authorization

[apiID](../README.md#apiID), [apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Callback Details |  -  |
**400** | Query or path params invalid |  -  |
**401** | Invalid API Key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_callbacks_event_patch**
> StatusResponse v4_callbacks_event_patch(event, channel, medium=medium, address=address, aws_data=aws_data)

Update Callback Details

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
    api_instance = smtpcom.CallbacksApi(api_client)
    event = 'event_example' # str | Event for which the callback should be created. Valid types are:  * delivered -  message delivered * failed - message bounced * complained - complaint received * bounceback - bounce back notification received * received - message received by our system * queued - message in queue (transient) * hard_bounced - hard bounce received * opened - message opened * clicked - URL in message clicked * unsubscribed - unsubscribe received 
channel = 'channel_example' # str | Name of the channel for which the callback has been created
medium = 'medium_example' # str | Medium by which the callback data is sent. Possible values are one of:   * http   * aws  (optional)
address = 'address_example' # str | Address to which the callback data is sent. This will be either a URL for http-based callbacks or the Amazon SQS queue name for SQS-based callbacks (optional)
aws_data = 'aws_data_example' # str | Amazon SQS settings. ``` {key:string, secret:string} ``` must be provided if medium is of type sqs  (optional)

    try:
        # Update Callback Details
        api_response = api_instance.v4_callbacks_event_patch(event, channel, medium=medium, address=address, aws_data=aws_data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CallbacksApi->v4_callbacks_event_patch: %s\n" % e)
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
    api_instance = smtpcom.CallbacksApi(api_client)
    event = 'event_example' # str | Event for which the callback should be created. Valid types are:  * delivered -  message delivered * failed - message bounced * complained - complaint received * bounceback - bounce back notification received * received - message received by our system * queued - message in queue (transient) * hard_bounced - hard bounce received * opened - message opened * clicked - URL in message clicked * unsubscribed - unsubscribe received 
channel = 'channel_example' # str | Name of the channel for which the callback has been created
medium = 'medium_example' # str | Medium by which the callback data is sent. Possible values are one of:   * http   * aws  (optional)
address = 'address_example' # str | Address to which the callback data is sent. This will be either a URL for http-based callbacks or the Amazon SQS queue name for SQS-based callbacks (optional)
aws_data = 'aws_data_example' # str | Amazon SQS settings. ``` {key:string, secret:string} ``` must be provided if medium is of type sqs  (optional)

    try:
        # Update Callback Details
        api_response = api_instance.v4_callbacks_event_patch(event, channel, medium=medium, address=address, aws_data=aws_data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CallbacksApi->v4_callbacks_event_patch: %s\n" % e)
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
    api_instance = smtpcom.CallbacksApi(api_client)
    event = 'event_example' # str | Event for which the callback should be created. Valid types are:  * delivered -  message delivered * failed - message bounced * complained - complaint received * bounceback - bounce back notification received * received - message received by our system * queued - message in queue (transient) * hard_bounced - hard bounce received * opened - message opened * clicked - URL in message clicked * unsubscribed - unsubscribe received 
channel = 'channel_example' # str | Name of the channel for which the callback has been created
medium = 'medium_example' # str | Medium by which the callback data is sent. Possible values are one of:   * http   * aws  (optional)
address = 'address_example' # str | Address to which the callback data is sent. This will be either a URL for http-based callbacks or the Amazon SQS queue name for SQS-based callbacks (optional)
aws_data = 'aws_data_example' # str | Amazon SQS settings. ``` {key:string, secret:string} ``` must be provided if medium is of type sqs  (optional)

    try:
        # Update Callback Details
        api_response = api_instance.v4_callbacks_event_patch(event, channel, medium=medium, address=address, aws_data=aws_data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CallbacksApi->v4_callbacks_event_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event** | **str**| Event for which the callback should be created. Valid types are:  * delivered -  message delivered * failed - message bounced * complained - complaint received * bounceback - bounce back notification received * received - message received by our system * queued - message in queue (transient) * hard_bounced - hard bounce received * opened - message opened * clicked - URL in message clicked * unsubscribed - unsubscribe received  | 
 **channel** | **str**| Name of the channel for which the callback has been created | 
 **medium** | **str**| Medium by which the callback data is sent. Possible values are one of:   * http   * aws  | [optional] 
 **address** | **str**| Address to which the callback data is sent. This will be either a URL for http-based callbacks or the Amazon SQS queue name for SQS-based callbacks | [optional] 
 **aws_data** | **str**| Amazon SQS settings. &#x60;&#x60;&#x60; {key:string, secret:string} &#x60;&#x60;&#x60; must be provided if medium is of type sqs  | [optional] 

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
**200** | Update Callback |  -  |
**400** | Query or path params invalid |  -  |
**401** | Invalid API Key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_callbacks_event_post**
> CreateCallbackResponse v4_callbacks_event_post(event, channel, medium, address, aws_data=aws_data)

Create Callback

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
    api_instance = smtpcom.CallbacksApi(api_client)
    event = 'event_example' # str | Event for which the callback should be created. Valid types are:  * delivered -  message delivered * failed - message bounced * complained - complaint received * bounceback - bounce back notification received * received - message received by our system * queued - message in queue (transient) * hard_bounced - hard bounce received * opened - message opened * clicked - URL in message clicked * unsubscribed - unsubscribe received 
channel = 'channel_example' # str | Name of the channel for which the callback has been created.
medium = 'medium_example' # str | Medium to send callback data. Valid values are one of:   * http   * sqs 
address = 'address_example' # str | Address of where the callback data should be sent. This will be either a URL for http-based callbacks or the Amazon SQS queue name for SQS-based callbacks.
aws_data = 'aws_data_example' # str | Amazon SQS settings. ``` {key:string, secret:string} ``` must be provided if medium is of type sqs  (optional)

    try:
        # Create Callback
        api_response = api_instance.v4_callbacks_event_post(event, channel, medium, address, aws_data=aws_data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CallbacksApi->v4_callbacks_event_post: %s\n" % e)
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
    api_instance = smtpcom.CallbacksApi(api_client)
    event = 'event_example' # str | Event for which the callback should be created. Valid types are:  * delivered -  message delivered * failed - message bounced * complained - complaint received * bounceback - bounce back notification received * received - message received by our system * queued - message in queue (transient) * hard_bounced - hard bounce received * opened - message opened * clicked - URL in message clicked * unsubscribed - unsubscribe received 
channel = 'channel_example' # str | Name of the channel for which the callback has been created.
medium = 'medium_example' # str | Medium to send callback data. Valid values are one of:   * http   * sqs 
address = 'address_example' # str | Address of where the callback data should be sent. This will be either a URL for http-based callbacks or the Amazon SQS queue name for SQS-based callbacks.
aws_data = 'aws_data_example' # str | Amazon SQS settings. ``` {key:string, secret:string} ``` must be provided if medium is of type sqs  (optional)

    try:
        # Create Callback
        api_response = api_instance.v4_callbacks_event_post(event, channel, medium, address, aws_data=aws_data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CallbacksApi->v4_callbacks_event_post: %s\n" % e)
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
    api_instance = smtpcom.CallbacksApi(api_client)
    event = 'event_example' # str | Event for which the callback should be created. Valid types are:  * delivered -  message delivered * failed - message bounced * complained - complaint received * bounceback - bounce back notification received * received - message received by our system * queued - message in queue (transient) * hard_bounced - hard bounce received * opened - message opened * clicked - URL in message clicked * unsubscribed - unsubscribe received 
channel = 'channel_example' # str | Name of the channel for which the callback has been created.
medium = 'medium_example' # str | Medium to send callback data. Valid values are one of:   * http   * sqs 
address = 'address_example' # str | Address of where the callback data should be sent. This will be either a URL for http-based callbacks or the Amazon SQS queue name for SQS-based callbacks.
aws_data = 'aws_data_example' # str | Amazon SQS settings. ``` {key:string, secret:string} ``` must be provided if medium is of type sqs  (optional)

    try:
        # Create Callback
        api_response = api_instance.v4_callbacks_event_post(event, channel, medium, address, aws_data=aws_data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CallbacksApi->v4_callbacks_event_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event** | **str**| Event for which the callback should be created. Valid types are:  * delivered -  message delivered * failed - message bounced * complained - complaint received * bounceback - bounce back notification received * received - message received by our system * queued - message in queue (transient) * hard_bounced - hard bounce received * opened - message opened * clicked - URL in message clicked * unsubscribed - unsubscribe received  | 
 **channel** | **str**| Name of the channel for which the callback has been created. | 
 **medium** | **str**| Medium to send callback data. Valid values are one of:   * http   * sqs  | 
 **address** | **str**| Address of where the callback data should be sent. This will be either a URL for http-based callbacks or the Amazon SQS queue name for SQS-based callbacks. | 
 **aws_data** | **str**| Amazon SQS settings. &#x60;&#x60;&#x60; {key:string, secret:string} &#x60;&#x60;&#x60; must be provided if medium is of type sqs  | [optional] 

### Return type

[**CreateCallbackResponse**](CreateCallbackResponse.md)

### Authorization

[apiID](../README.md#apiID), [apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Create Callback |  -  |
**400** | Query or path params invalid |  -  |
**401** | Invalid API Key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_callbacks_get**
> GetCallbackResponse v4_callbacks_get()

List All Callbacks

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
    api_instance = smtpcom.CallbacksApi(api_client)
    
    try:
        # List All Callbacks
        api_response = api_instance.v4_callbacks_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CallbacksApi->v4_callbacks_get: %s\n" % e)
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
    api_instance = smtpcom.CallbacksApi(api_client)
    
    try:
        # List All Callbacks
        api_response = api_instance.v4_callbacks_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CallbacksApi->v4_callbacks_get: %s\n" % e)
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
    api_instance = smtpcom.CallbacksApi(api_client)
    
    try:
        # List All Callbacks
        api_response = api_instance.v4_callbacks_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CallbacksApi->v4_callbacks_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetCallbackResponse**](GetCallbackResponse.md)

### Authorization

[apiID](../README.md#apiID), [apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List All Callbacks |  -  |
**400** | Query or path params invalid |  -  |
**401** | Invalid API Key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_callbacks_log_get**
> GetCallbackLogs v4_callbacks_log_get(channel, limit=limit)

View Callback Logs

Review all callback logs for a specific channel. It may help debug issues related to receiving callbacks on a user's side.

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
    api_instance = smtpcom.CallbacksApi(api_client)
    channel = 'channel_example' # str | Name of the channel for which the given callback has been created
limit = 56 # int | Number of items to return in the response. Default is 20 (optional)

    try:
        # View Callback Logs
        api_response = api_instance.v4_callbacks_log_get(channel, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CallbacksApi->v4_callbacks_log_get: %s\n" % e)
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
    api_instance = smtpcom.CallbacksApi(api_client)
    channel = 'channel_example' # str | Name of the channel for which the given callback has been created
limit = 56 # int | Number of items to return in the response. Default is 20 (optional)

    try:
        # View Callback Logs
        api_response = api_instance.v4_callbacks_log_get(channel, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CallbacksApi->v4_callbacks_log_get: %s\n" % e)
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
    api_instance = smtpcom.CallbacksApi(api_client)
    channel = 'channel_example' # str | Name of the channel for which the given callback has been created
limit = 56 # int | Number of items to return in the response. Default is 20 (optional)

    try:
        # View Callback Logs
        api_response = api_instance.v4_callbacks_log_get(channel, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CallbacksApi->v4_callbacks_log_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel** | **str**| Name of the channel for which the given callback has been created | 
 **limit** | **int**| Number of items to return in the response. Default is 20 | [optional] 

### Return type

[**GetCallbackLogs**](GetCallbackLogs.md)

### Authorization

[apiID](../README.md#apiID), [apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | View Callback Logs |  -  |
**400** | Query or path params invalid |  -  |
**401** | Invalid API Key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

