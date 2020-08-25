# smtp.MessagesApi

All URIs are relative to *https://api.smtp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v4_messages_get**](MessagesApi.md#v4_messages_get) | **GET** /v4/messages | Get Detailed Messages Info
[**v4_messages_mime_post**](MessagesApi.md#v4_messages_mime_post) | **POST** /v4/messages/mime | Send MIME Message
[**v4_messages_post**](MessagesApi.md#v4_messages_post) | **POST** /v4/messages | Send a Message


# **v4_messages_get**
> MessagesResponse v4_messages_get(start, limit, offset, channel, end=end, event=event, msg_id=msg_id)

Get Detailed Messages Info

### Example

* Api Key Authentication (apiID):
```python
from __future__ import print_function
import time
import smtp
from smtp.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.smtp.com
# See configuration.py for a list of all supported configuration parameters.
configuration = smtp.Configuration(
    host = "https://api.smtp.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiID
configuration = smtp.Configuration(
    host = "https://api.smtp.com",
    api_key = {
        'apiID': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiID'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = smtp.Configuration(
    host = "https://api.smtp.com",
    api_key = {
        'apiKey': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure HTTP basic authorization: basicAuth
configuration = smtp.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with smtp.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = smtp.MessagesApi(api_client)
    start = 'start_example' # str | The starting time. RFC 2822 or UNIX epoch format
limit = 56 # int | Maximum number of items to return.
offset = 56 # int | Number of items to skip before returning the results.
channel = 'channel_example' # str | Name of  the channel used to send messages
end = 'end_example' # str | The ending time. If not specified, defaults to now. RFC 2822 or UNIX epoch format. (optional)
event = 'event_example' # str | Array of any event names for which stats has been requested ('accepted', 'failed', 'delivered'). (optional)
msg_id = 'msg_id_example' # str | Unique message ID (optional)

    try:
        # Get Detailed Messages Info
        api_response = api_instance.v4_messages_get(start, limit, offset, channel, end=end, event=event, msg_id=msg_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MessagesApi->v4_messages_get: %s\n" % e)
```

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import smtp
from smtp.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.smtp.com
# See configuration.py for a list of all supported configuration parameters.
configuration = smtp.Configuration(
    host = "https://api.smtp.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiID
configuration = smtp.Configuration(
    host = "https://api.smtp.com",
    api_key = {
        'apiID': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiID'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = smtp.Configuration(
    host = "https://api.smtp.com",
    api_key = {
        'apiKey': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure HTTP basic authorization: basicAuth
configuration = smtp.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with smtp.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = smtp.MessagesApi(api_client)
    start = 'start_example' # str | The starting time. RFC 2822 or UNIX epoch format
limit = 56 # int | Maximum number of items to return.
offset = 56 # int | Number of items to skip before returning the results.
channel = 'channel_example' # str | Name of  the channel used to send messages
end = 'end_example' # str | The ending time. If not specified, defaults to now. RFC 2822 or UNIX epoch format. (optional)
event = 'event_example' # str | Array of any event names for which stats has been requested ('accepted', 'failed', 'delivered'). (optional)
msg_id = 'msg_id_example' # str | Unique message ID (optional)

    try:
        # Get Detailed Messages Info
        api_response = api_instance.v4_messages_get(start, limit, offset, channel, end=end, event=event, msg_id=msg_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MessagesApi->v4_messages_get: %s\n" % e)
```

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import smtp
from smtp.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.smtp.com
# See configuration.py for a list of all supported configuration parameters.
configuration = smtp.Configuration(
    host = "https://api.smtp.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiID
configuration = smtp.Configuration(
    host = "https://api.smtp.com",
    api_key = {
        'apiID': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiID'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = smtp.Configuration(
    host = "https://api.smtp.com",
    api_key = {
        'apiKey': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure HTTP basic authorization: basicAuth
configuration = smtp.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with smtp.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = smtp.MessagesApi(api_client)
    start = 'start_example' # str | The starting time. RFC 2822 or UNIX epoch format
limit = 56 # int | Maximum number of items to return.
offset = 56 # int | Number of items to skip before returning the results.
channel = 'channel_example' # str | Name of  the channel used to send messages
end = 'end_example' # str | The ending time. If not specified, defaults to now. RFC 2822 or UNIX epoch format. (optional)
event = 'event_example' # str | Array of any event names for which stats has been requested ('accepted', 'failed', 'delivered'). (optional)
msg_id = 'msg_id_example' # str | Unique message ID (optional)

    try:
        # Get Detailed Messages Info
        api_response = api_instance.v4_messages_get(start, limit, offset, channel, end=end, event=event, msg_id=msg_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MessagesApi->v4_messages_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **str**| The starting time. RFC 2822 or UNIX epoch format | 
 **limit** | **int**| Maximum number of items to return. | 
 **offset** | **int**| Number of items to skip before returning the results. | 
 **channel** | **str**| Name of  the channel used to send messages | 
 **end** | **str**| The ending time. If not specified, defaults to now. RFC 2822 or UNIX epoch format. | [optional] 
 **event** | **str**| Array of any event names for which stats has been requested (&#39;accepted&#39;, &#39;failed&#39;, &#39;delivered&#39;). | [optional] 
 **msg_id** | **str**| Unique message ID | [optional] 

### Return type

[**MessagesResponse**](MessagesResponse.md)

### Authorization

[apiID](../README.md#apiID), [apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Detailed Messages Info |  -  |
**400** | Query or path params invalid |  -  |
**401** | Invalid API Key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_messages_mime_post**
> MimeResponse v4_messages_mime_post(inline_object1)

Send MIME Message

This method will send a prepared RFC compliant MIME message via a specified channel **Note:** All restrictions from the section entitled `Send a Message` are implied here. 

### Example

* Api Key Authentication (apiID):
```python
from __future__ import print_function
import time
import smtp
from smtp.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.smtp.com
# See configuration.py for a list of all supported configuration parameters.
configuration = smtp.Configuration(
    host = "https://api.smtp.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiID
configuration = smtp.Configuration(
    host = "https://api.smtp.com",
    api_key = {
        'apiID': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiID'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = smtp.Configuration(
    host = "https://api.smtp.com",
    api_key = {
        'apiKey': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure HTTP basic authorization: basicAuth
configuration = smtp.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with smtp.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = smtp.MessagesApi(api_client)
    inline_object1 = smtp.InlineObject1() # InlineObject1 | 

    try:
        # Send MIME Message
        api_response = api_instance.v4_messages_mime_post(inline_object1)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MessagesApi->v4_messages_mime_post: %s\n" % e)
```

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import smtp
from smtp.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.smtp.com
# See configuration.py for a list of all supported configuration parameters.
configuration = smtp.Configuration(
    host = "https://api.smtp.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiID
configuration = smtp.Configuration(
    host = "https://api.smtp.com",
    api_key = {
        'apiID': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiID'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = smtp.Configuration(
    host = "https://api.smtp.com",
    api_key = {
        'apiKey': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure HTTP basic authorization: basicAuth
configuration = smtp.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with smtp.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = smtp.MessagesApi(api_client)
    inline_object1 = smtp.InlineObject1() # InlineObject1 | 

    try:
        # Send MIME Message
        api_response = api_instance.v4_messages_mime_post(inline_object1)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MessagesApi->v4_messages_mime_post: %s\n" % e)
```

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import smtp
from smtp.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.smtp.com
# See configuration.py for a list of all supported configuration parameters.
configuration = smtp.Configuration(
    host = "https://api.smtp.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiID
configuration = smtp.Configuration(
    host = "https://api.smtp.com",
    api_key = {
        'apiID': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiID'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = smtp.Configuration(
    host = "https://api.smtp.com",
    api_key = {
        'apiKey': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure HTTP basic authorization: basicAuth
configuration = smtp.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with smtp.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = smtp.MessagesApi(api_client)
    inline_object1 = smtp.InlineObject1() # InlineObject1 | 

    try:
        # Send MIME Message
        api_response = api_instance.v4_messages_mime_post(inline_object1)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MessagesApi->v4_messages_mime_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object1** | [**InlineObject1**](InlineObject1.md)|  | 

### Return type

[**MimeResponse**](MimeResponse.md)

### Authorization

[apiID](../README.md#apiID), [apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Send MIME Message |  -  |
**400** | Query or path params invalid |  -  |
**401** | Invalid API Key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_messages_post**
> PostMessageResponse v4_messages_post(inline_object=inline_object)

Send a Message

Send a message over HTTP/HTTPS protocol using a specified channel. The request can generate only an HTTP 400 error and will return validation error data. The actual suppression, delivery attempt or SMTP error can be received via callbacks. See the section on Callbacks for more details.  <br> **Limitations:** * The number of recipients in a single email request is limited to `1000` (including to, cc and bcc) * The total payload of the generated MIME message cannot exceed `10Mb` in size  <br> **Notes:** * When JUST two parts provided with `text/plain` and `text/html` types, they are automatically wrapped into a `mime/alternative` container * Adding any other part or attachment to either a single part or attachment or `mime/alternative` automatically wraps all mime containers into a `mime/mixed` container * Content type message/rfc822 is prohibited 

### Example

* Api Key Authentication (apiID):
```python
from __future__ import print_function
import time
import smtp
from smtp.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.smtp.com
# See configuration.py for a list of all supported configuration parameters.
configuration = smtp.Configuration(
    host = "https://api.smtp.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiID
configuration = smtp.Configuration(
    host = "https://api.smtp.com",
    api_key = {
        'apiID': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiID'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = smtp.Configuration(
    host = "https://api.smtp.com",
    api_key = {
        'apiKey': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure HTTP basic authorization: basicAuth
configuration = smtp.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with smtp.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = smtp.MessagesApi(api_client)
    inline_object = smtp.InlineObject() # InlineObject |  (optional)

    try:
        # Send a Message
        api_response = api_instance.v4_messages_post(inline_object=inline_object)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MessagesApi->v4_messages_post: %s\n" % e)
```

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import smtp
from smtp.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.smtp.com
# See configuration.py for a list of all supported configuration parameters.
configuration = smtp.Configuration(
    host = "https://api.smtp.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiID
configuration = smtp.Configuration(
    host = "https://api.smtp.com",
    api_key = {
        'apiID': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiID'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = smtp.Configuration(
    host = "https://api.smtp.com",
    api_key = {
        'apiKey': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure HTTP basic authorization: basicAuth
configuration = smtp.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with smtp.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = smtp.MessagesApi(api_client)
    inline_object = smtp.InlineObject() # InlineObject |  (optional)

    try:
        # Send a Message
        api_response = api_instance.v4_messages_post(inline_object=inline_object)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MessagesApi->v4_messages_post: %s\n" % e)
```

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import smtp
from smtp.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.smtp.com
# See configuration.py for a list of all supported configuration parameters.
configuration = smtp.Configuration(
    host = "https://api.smtp.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiID
configuration = smtp.Configuration(
    host = "https://api.smtp.com",
    api_key = {
        'apiID': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiID'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = smtp.Configuration(
    host = "https://api.smtp.com",
    api_key = {
        'apiKey': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure HTTP basic authorization: basicAuth
configuration = smtp.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with smtp.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = smtp.MessagesApi(api_client)
    inline_object = smtp.InlineObject() # InlineObject |  (optional)

    try:
        # Send a Message
        api_response = api_instance.v4_messages_post(inline_object=inline_object)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MessagesApi->v4_messages_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object** | [**InlineObject**](InlineObject.md)|  | [optional] 

### Return type

[**PostMessageResponse**](PostMessageResponse.md)

### Authorization

[apiID](../README.md#apiID), [apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Send a Message |  -  |
**400** | Query or path params invalid |  -  |
**401** | Invalid API Key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

