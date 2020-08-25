# smtp.ChannelsApi

All URIs are relative to *https://api.smtp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sender**](ChannelsApi.md#get_sender) | **GET** /v4/channels/{name} | Get Channel Details
[**v4_channels_get**](ChannelsApi.md#v4_channels_get) | **GET** /v4/channels/ | Get All Channels
[**v4_channels_name_delete**](ChannelsApi.md#v4_channels_name_delete) | **DELETE** /v4/channels/{name} | Delete a Channel
[**v4_channels_name_patch**](ChannelsApi.md#v4_channels_name_patch) | **PATCH** /v4/channels/{name} | Update Channel Details
[**v4_channels_post**](ChannelsApi.md#v4_channels_post) | **POST** /v4/channels/ | Create a New Channel


# **get_sender**
> Channel get_sender(name)

Get Channel Details

**Note:** This method doesn't return archived channels. 

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
    api_instance = smtp.ChannelsApi(api_client)
    name = 'name_example' # str | Name of the channel (sender)

    try:
        # Get Channel Details
        api_response = api_instance.get_sender(name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChannelsApi->get_sender: %s\n" % e)
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
    api_instance = smtp.ChannelsApi(api_client)
    name = 'name_example' # str | Name of the channel (sender)

    try:
        # Get Channel Details
        api_response = api_instance.get_sender(name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChannelsApi->get_sender: %s\n" % e)
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
    api_instance = smtp.ChannelsApi(api_client)
    name = 'name_example' # str | Name of the channel (sender)

    try:
        # Get Channel Details
        api_response = api_instance.get_sender(name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChannelsApi->get_sender: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the channel (sender) | 

### Return type

[**Channel**](Channel.md)

### Authorization

[apiID](../README.md#apiID), [apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Channel Details |  -  |
**400** | Query or path params invalid |  -  |
**401** | Invalid API Key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_channels_get**
> Channels v4_channels_get()

Get All Channels

**Note:** This method does not return archived channels. 

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
    api_instance = smtp.ChannelsApi(api_client)
    
    try:
        # Get All Channels
        api_response = api_instance.v4_channels_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChannelsApi->v4_channels_get: %s\n" % e)
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
    api_instance = smtp.ChannelsApi(api_client)
    
    try:
        # Get All Channels
        api_response = api_instance.v4_channels_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChannelsApi->v4_channels_get: %s\n" % e)
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
    api_instance = smtp.ChannelsApi(api_client)
    
    try:
        # Get All Channels
        api_response = api_instance.v4_channels_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChannelsApi->v4_channels_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Channels**](Channels.md)

### Authorization

[apiID](../README.md#apiID), [apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get All Channels |  -  |
**400** | Query or path params invalid |  -  |
**401** | Invalid API Key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_channels_name_delete**
> Channel v4_channels_name_delete(name)

Delete a Channel

**Note:** This method doesn’t permanently delete the channel but rather sets the status to “canceled”. 

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
    api_instance = smtp.ChannelsApi(api_client)
    name = 'name_example' # str | Name of the channel (sender)

    try:
        # Delete a Channel
        api_response = api_instance.v4_channels_name_delete(name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChannelsApi->v4_channels_name_delete: %s\n" % e)
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
    api_instance = smtp.ChannelsApi(api_client)
    name = 'name_example' # str | Name of the channel (sender)

    try:
        # Delete a Channel
        api_response = api_instance.v4_channels_name_delete(name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChannelsApi->v4_channels_name_delete: %s\n" % e)
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
    api_instance = smtp.ChannelsApi(api_client)
    name = 'name_example' # str | Name of the channel (sender)

    try:
        # Delete a Channel
        api_response = api_instance.v4_channels_name_delete(name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChannelsApi->v4_channels_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the channel (sender) | 

### Return type

[**Channel**](Channel.md)

### Authorization

[apiID](../README.md#apiID), [apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete a Channel |  -  |
**400** | Query or path params invalid |  -  |
**401** | Invalid API Key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_channels_name_patch**
> Channel v4_channels_name_patch(name, smtp_username=smtp_username, smtp_password=smtp_password, quota=quota)

Update Channel Details

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
    api_instance = smtp.ChannelsApi(api_client)
    name = 'name_example' # str | Name of the channel (sender)
smtp_username = 'smtp_username_example' # str | Username for the channel (optional)
smtp_password = 'smtp_password_example' # str | Password for the channel (optional)
quota = 56 # int | Quota for the channel (optional)

    try:
        # Update Channel Details
        api_response = api_instance.v4_channels_name_patch(name, smtp_username=smtp_username, smtp_password=smtp_password, quota=quota)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChannelsApi->v4_channels_name_patch: %s\n" % e)
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
    api_instance = smtp.ChannelsApi(api_client)
    name = 'name_example' # str | Name of the channel (sender)
smtp_username = 'smtp_username_example' # str | Username for the channel (optional)
smtp_password = 'smtp_password_example' # str | Password for the channel (optional)
quota = 56 # int | Quota for the channel (optional)

    try:
        # Update Channel Details
        api_response = api_instance.v4_channels_name_patch(name, smtp_username=smtp_username, smtp_password=smtp_password, quota=quota)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChannelsApi->v4_channels_name_patch: %s\n" % e)
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
    api_instance = smtp.ChannelsApi(api_client)
    name = 'name_example' # str | Name of the channel (sender)
smtp_username = 'smtp_username_example' # str | Username for the channel (optional)
smtp_password = 'smtp_password_example' # str | Password for the channel (optional)
quota = 56 # int | Quota for the channel (optional)

    try:
        # Update Channel Details
        api_response = api_instance.v4_channels_name_patch(name, smtp_username=smtp_username, smtp_password=smtp_password, quota=quota)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChannelsApi->v4_channels_name_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the channel (sender) | 
 **smtp_username** | **str**| Username for the channel | [optional] 
 **smtp_password** | **str**| Password for the channel | [optional] 
 **quota** | **int**| Quota for the channel | [optional] 

### Return type

[**Channel**](Channel.md)

### Authorization

[apiID](../README.md#apiID), [apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update Channel Details |  -  |
**400** | Query or path params invalid |  -  |
**401** | Invalid API Key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_channels_post**
> Channel v4_channels_post(name, smtp_username, smtp_password, quota)

Create a New Channel

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
    api_instance = smtp.ChannelsApi(api_client)
    name = 'name_example' # str | Name of the channel (sender)
smtp_username = 'smtp_username_example' # str | Username for the channel
smtp_password = 'smtp_password_example' # str | Password for the channel
quota = 56 # int | Quota for the channel

    try:
        # Create a New Channel
        api_response = api_instance.v4_channels_post(name, smtp_username, smtp_password, quota)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChannelsApi->v4_channels_post: %s\n" % e)
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
    api_instance = smtp.ChannelsApi(api_client)
    name = 'name_example' # str | Name of the channel (sender)
smtp_username = 'smtp_username_example' # str | Username for the channel
smtp_password = 'smtp_password_example' # str | Password for the channel
quota = 56 # int | Quota for the channel

    try:
        # Create a New Channel
        api_response = api_instance.v4_channels_post(name, smtp_username, smtp_password, quota)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChannelsApi->v4_channels_post: %s\n" % e)
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
    api_instance = smtp.ChannelsApi(api_client)
    name = 'name_example' # str | Name of the channel (sender)
smtp_username = 'smtp_username_example' # str | Username for the channel
smtp_password = 'smtp_password_example' # str | Password for the channel
quota = 56 # int | Quota for the channel

    try:
        # Create a New Channel
        api_response = api_instance.v4_channels_post(name, smtp_username, smtp_password, quota)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChannelsApi->v4_channels_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the channel (sender) | 
 **smtp_username** | **str**| Username for the channel | 
 **smtp_password** | **str**| Password for the channel | 
 **quota** | **int**| Quota for the channel | 

### Return type

[**Channel**](Channel.md)

### Authorization

[apiID](../README.md#apiID), [apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Create a New Channel |  -  |
**400** | Query or path params invalid |  -  |
**401** | Invalid API Key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

