# smtp.AccountApi

All URIs are relative to *https://api.smtp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v4_account_contact_patch**](AccountApi.md#v4_account_contact_patch) | **PATCH** /v4/account/contact | Update Account Details
[**v4_account_get**](AccountApi.md#v4_account_get) | **GET** /v4/account/ | Get Account Details


# **v4_account_contact_patch**
> UpdateAccountResponse v4_account_contact_patch(first_name=first_name, last_name=last_name, email=email, company_name=company_name, phone=phone, website=website, address_street=address_street, address_city=address_city, address_state=address_state, address_country=address_country)

Update Account Details

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
    api_instance = smtp.AccountApi(api_client)
    first_name = 'first_name_example' # str | First name of account owner (optional)
last_name = 'last_name_example' # str | Last name of account owner (optional)
email = 'email_example' # str | Email address of account owner (optional)
company_name = 'company_name_example' # str | Account owner’s company name (optional)
phone = 'phone_example' # str | Phone number of account owner (optional)
website = 'website_example' # str | Website of account owner (optional)
address_street = 'address_street_example' # str | Account owner’s street address (optional)
address_city = 'address_city_example' # str | Account owner’s city (optional)
address_state = 'address_state_example' # str | Account owner’s state (optional)
address_country = 'address_country_example' # str | Account owner’s country (optional)

    try:
        # Update Account Details
        api_response = api_instance.v4_account_contact_patch(first_name=first_name, last_name=last_name, email=email, company_name=company_name, phone=phone, website=website, address_street=address_street, address_city=address_city, address_state=address_state, address_country=address_country)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->v4_account_contact_patch: %s\n" % e)
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
    api_instance = smtp.AccountApi(api_client)
    first_name = 'first_name_example' # str | First name of account owner (optional)
last_name = 'last_name_example' # str | Last name of account owner (optional)
email = 'email_example' # str | Email address of account owner (optional)
company_name = 'company_name_example' # str | Account owner’s company name (optional)
phone = 'phone_example' # str | Phone number of account owner (optional)
website = 'website_example' # str | Website of account owner (optional)
address_street = 'address_street_example' # str | Account owner’s street address (optional)
address_city = 'address_city_example' # str | Account owner’s city (optional)
address_state = 'address_state_example' # str | Account owner’s state (optional)
address_country = 'address_country_example' # str | Account owner’s country (optional)

    try:
        # Update Account Details
        api_response = api_instance.v4_account_contact_patch(first_name=first_name, last_name=last_name, email=email, company_name=company_name, phone=phone, website=website, address_street=address_street, address_city=address_city, address_state=address_state, address_country=address_country)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->v4_account_contact_patch: %s\n" % e)
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
    api_instance = smtp.AccountApi(api_client)
    first_name = 'first_name_example' # str | First name of account owner (optional)
last_name = 'last_name_example' # str | Last name of account owner (optional)
email = 'email_example' # str | Email address of account owner (optional)
company_name = 'company_name_example' # str | Account owner’s company name (optional)
phone = 'phone_example' # str | Phone number of account owner (optional)
website = 'website_example' # str | Website of account owner (optional)
address_street = 'address_street_example' # str | Account owner’s street address (optional)
address_city = 'address_city_example' # str | Account owner’s city (optional)
address_state = 'address_state_example' # str | Account owner’s state (optional)
address_country = 'address_country_example' # str | Account owner’s country (optional)

    try:
        # Update Account Details
        api_response = api_instance.v4_account_contact_patch(first_name=first_name, last_name=last_name, email=email, company_name=company_name, phone=phone, website=website, address_street=address_street, address_city=address_city, address_state=address_state, address_country=address_country)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->v4_account_contact_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **first_name** | **str**| First name of account owner | [optional] 
 **last_name** | **str**| Last name of account owner | [optional] 
 **email** | **str**| Email address of account owner | [optional] 
 **company_name** | **str**| Account owner’s company name | [optional] 
 **phone** | **str**| Phone number of account owner | [optional] 
 **website** | **str**| Website of account owner | [optional] 
 **address_street** | **str**| Account owner’s street address | [optional] 
 **address_city** | **str**| Account owner’s city | [optional] 
 **address_state** | **str**| Account owner’s state | [optional] 
 **address_country** | **str**| Account owner’s country | [optional] 

### Return type

[**UpdateAccountResponse**](UpdateAccountResponse.md)

### Authorization

[apiID](../README.md#apiID), [apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update Account Details |  -  |
**400** | Query or path params invalid |  -  |
**401** | Invalid API Key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_account_get**
> Account v4_account_get()

Get Account Details

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
    api_instance = smtp.AccountApi(api_client)
    
    try:
        # Get Account Details
        api_response = api_instance.v4_account_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->v4_account_get: %s\n" % e)
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
    api_instance = smtp.AccountApi(api_client)
    
    try:
        # Get Account Details
        api_response = api_instance.v4_account_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->v4_account_get: %s\n" % e)
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
    api_instance = smtp.AccountApi(api_client)
    
    try:
        # Get Account Details
        api_response = api_instance.v4_account_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->v4_account_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Account**](Account.md)

### Authorization

[apiID](../README.md#apiID), [apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Account Details |  -  |
**400** | Query or path params invalid |  -  |
**401** | Invalid API Key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

