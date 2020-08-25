# smtp.APIKeysApi

All URIs are relative to *https://api.smtp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_key**](APIKeysApi.md#get_api_key) | **GET** /v4/api_keys/{api_key} | Get API Key Details
[**v4_api_keys_api_key_delete**](APIKeysApi.md#v4_api_keys_api_key_delete) | **DELETE** /v4/api_keys/{api_key} | Delete an API Key
[**v4_api_keys_api_key_patch**](APIKeysApi.md#v4_api_keys_api_key_patch) | **PATCH** /v4/api_keys/{api_key} | Update API Key
[**v4_api_keys_get**](APIKeysApi.md#v4_api_keys_get) | **GET** /v4/api_keys/ | List All API Keys
[**v4_api_keys_post**](APIKeysApi.md#v4_api_keys_post) | **POST** /v4/api_keys/ | Create a New API Key


# **get_api_key**
> APIKey get_api_key(api_key)

Get API Key Details

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
    api_instance = smtp.APIKeysApi(api_client)
    api_key = 'api_key_example' # str | API Key Identificator.

    try:
        # Get API Key Details
        api_response = api_instance.get_api_key(api_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling APIKeysApi->get_api_key: %s\n" % e)
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
    api_instance = smtp.APIKeysApi(api_client)
    api_key = 'api_key_example' # str | API Key Identificator.

    try:
        # Get API Key Details
        api_response = api_instance.get_api_key(api_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling APIKeysApi->get_api_key: %s\n" % e)
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
    api_instance = smtp.APIKeysApi(api_client)
    api_key = 'api_key_example' # str | API Key Identificator.

    try:
        # Get API Key Details
        api_response = api_instance.get_api_key(api_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling APIKeysApi->get_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| API Key Identificator. | 

### Return type

[**APIKey**](APIKey.md)

### Authorization

[apiID](../README.md#apiID), [apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get API Key |  -  |
**400** | Query or path params invalid |  -  |
**401** | Invalid API Key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_api_keys_api_key_delete**
> StatusResponse v4_api_keys_api_key_delete(api_key)

Delete an API Key

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
    api_instance = smtp.APIKeysApi(api_client)
    api_key = 'api_key_example' # str | API key value

    try:
        # Delete an API Key
        api_response = api_instance.v4_api_keys_api_key_delete(api_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling APIKeysApi->v4_api_keys_api_key_delete: %s\n" % e)
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
    api_instance = smtp.APIKeysApi(api_client)
    api_key = 'api_key_example' # str | API key value

    try:
        # Delete an API Key
        api_response = api_instance.v4_api_keys_api_key_delete(api_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling APIKeysApi->v4_api_keys_api_key_delete: %s\n" % e)
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
    api_instance = smtp.APIKeysApi(api_client)
    api_key = 'api_key_example' # str | API key value

    try:
        # Delete an API Key
        api_response = api_instance.v4_api_keys_api_key_delete(api_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling APIKeysApi->v4_api_keys_api_key_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| API key value | 

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
**200** | Delete an API Key |  -  |
**400** | Query or path params invalid |  -  |
**401** | Invalid API Key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_api_keys_api_key_patch**
> APIKey v4_api_keys_api_key_patch(api_key, name=name, description=description)

Update API Key

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
    api_instance = smtp.APIKeysApi(api_client)
    api_key = 'api_key_example' # str | API key value
name = 'name_example' # str | Name for API key (optional)
description = 'description_example' # str | Description for API Key (optional)

    try:
        # Update API Key
        api_response = api_instance.v4_api_keys_api_key_patch(api_key, name=name, description=description)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling APIKeysApi->v4_api_keys_api_key_patch: %s\n" % e)
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
    api_instance = smtp.APIKeysApi(api_client)
    api_key = 'api_key_example' # str | API key value
name = 'name_example' # str | Name for API key (optional)
description = 'description_example' # str | Description for API Key (optional)

    try:
        # Update API Key
        api_response = api_instance.v4_api_keys_api_key_patch(api_key, name=name, description=description)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling APIKeysApi->v4_api_keys_api_key_patch: %s\n" % e)
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
    api_instance = smtp.APIKeysApi(api_client)
    api_key = 'api_key_example' # str | API key value
name = 'name_example' # str | Name for API key (optional)
description = 'description_example' # str | Description for API Key (optional)

    try:
        # Update API Key
        api_response = api_instance.v4_api_keys_api_key_patch(api_key, name=name, description=description)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling APIKeysApi->v4_api_keys_api_key_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| API key value | 
 **name** | **str**| Name for API key | [optional] 
 **description** | **str**| Description for API Key | [optional] 

### Return type

[**APIKey**](APIKey.md)

### Authorization

[apiID](../README.md#apiID), [apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update API Key |  -  |
**400** | Query or path params invalid |  -  |
**401** | Invalid API Key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_api_keys_get**
> GetApiKeys v4_api_keys_get()

List All API Keys

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
    api_instance = smtp.APIKeysApi(api_client)
    
    try:
        # List All API Keys
        api_response = api_instance.v4_api_keys_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling APIKeysApi->v4_api_keys_get: %s\n" % e)
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
    api_instance = smtp.APIKeysApi(api_client)
    
    try:
        # List All API Keys
        api_response = api_instance.v4_api_keys_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling APIKeysApi->v4_api_keys_get: %s\n" % e)
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
    api_instance = smtp.APIKeysApi(api_client)
    
    try:
        # List All API Keys
        api_response = api_instance.v4_api_keys_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling APIKeysApi->v4_api_keys_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetApiKeys**](GetApiKeys.md)

### Authorization

[apiID](../README.md#apiID), [apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List All API Keys |  -  |
**400** | Query or path params invalid |  -  |
**401** | Invalid API Key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_api_keys_post**
> APIKey v4_api_keys_post(name, description=description)

Create a New API Key

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
    api_instance = smtp.APIKeysApi(api_client)
    name = 'name_example' # str | Name for API key
description = 'description_example' # str | Description for API key (optional)

    try:
        # Create a New API Key
        api_response = api_instance.v4_api_keys_post(name, description=description)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling APIKeysApi->v4_api_keys_post: %s\n" % e)
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
    api_instance = smtp.APIKeysApi(api_client)
    name = 'name_example' # str | Name for API key
description = 'description_example' # str | Description for API key (optional)

    try:
        # Create a New API Key
        api_response = api_instance.v4_api_keys_post(name, description=description)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling APIKeysApi->v4_api_keys_post: %s\n" % e)
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
    api_instance = smtp.APIKeysApi(api_client)
    name = 'name_example' # str | Name for API key
description = 'description_example' # str | Description for API key (optional)

    try:
        # Create a New API Key
        api_response = api_instance.v4_api_keys_post(name, description=description)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling APIKeysApi->v4_api_keys_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name for API key | 
 **description** | **str**| Description for API key | [optional] 

### Return type

[**APIKey**](APIKey.md)

### Authorization

[apiID](../README.md#apiID), [apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Create a New API Key |  -  |
**400** | Query or path params invalid |  -  |
**401** | Invalid API Key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

