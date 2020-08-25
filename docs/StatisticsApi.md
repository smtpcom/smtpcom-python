# smtp.StatisticsApi

All URIs are relative to *https://api.smtp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v4_stats_duration_slice_slice_specifier_group_by_get**](StatisticsApi.md#v4_stats_duration_slice_slice_specifier_group_by_get) | **GET** /v4/stats/{duration}/{slice}/{slice_specifier}/{group_by} | Return event aggregates for the specified slices and duration. Slices can be chained.


# **v4_stats_duration_slice_slice_specifier_group_by_get**
> StatsResponse v4_stats_duration_slice_slice_specifier_group_by_get(start, duration, slice, slice_specifier, group_by, limit, offset, end=end, event=event)

Return event aggregates for the specified slices and duration. Slices can be chained.

**Get stats for a period**<br> Request:<br> */v4/stats/last_day*<br> */v4/stats?start=Tue%2C%2016%20Jan%2015%3A14%3A29%20%2B0000*<br> Response:<br> ``` {\"accepted\": 300, \"delivered\": 100, \"complained\": 0, \"failed\": 50, \"bounced\": 150, \"queued\": 0} ``` <br><br> **Get stats for a period, grouped by channel**<br> Request:<br> */v4/stats/last_day/channel*<br> Response:<br> ``` {\"channel1\": {\"accepted\": 30, \"delivered\": 10, \"complained\": 0, \"failed\": 5, \"bounced\": 15, \"queued\": 0}, \"channel2\": {\"accepted\": 0, \"delivered\": 0, \"complained\": 0, \"failed\": 0, \"bounced\": 0, \"queued\": 0}} ``` <br><br> **Get stats for specific sending domain and channel (sender) and period, grouped by ISP**<br> Request:<br> */v4/stats/last_day/channel/marketing/domain/smtp.com/rcpt_isp*<br> Response:<br> ``` {\"yahoo\": {\"accepted\": 30, \"delivered\": 10, \"complained\": 0, \"failed\": 5, \"bounced\": 15, \"queued\": 0}, \"google\": {\"accepted\": 0, \"delivered\": 0, \"complained\": 0, \"failed\": 0, \"bounced\": 0, \"queued\": 0}} ``` 

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
    api_instance = smtp.StatisticsApi(api_client)
    start = 'start_example' # str | The starting time. Required if the `{duration}` path parameter is not specified. RFC 2822 or UNIX epoch format.
duration = 'duration_example' # str | A standardized shorthand for a known start/end bracket. Duration automatically supersedes start/end values provided as query string parameters. One of either the `{duration}` path parameter or the `start` query parameter must be specified.  <table>  <tr><th>Value</th><th>Start</th><th>End</th><th>Slicable</th></tr>  <tr><td>last_24hrs</td><td>84,400 seconds ago</td><td>Now</td><td>yes</td></tr>  <tr><td>last_30days</td><td>18,144,000 seconds ago</td><td>Now</td><td>yes</td></tr>  <tr><td>last_7days</td><td>604,800 seconds ago</td><td>Now</td><td>yes</td></tr>  <tr><td>last_day</td><td>00:00:00 of the previous day</td><td>23:59:59 of the previous day</td><td>yes</td></tr>  <tr><td>last_hour</td><td>00:00 of the previous hour</td><td>59:59 of the previous hour</td><td>yes</td></tr>  <tr><td>last_month or mtd</td><td>1st day 00:00:00 of previous month</td><td>23:59:59 last day of previous month</td><td>yes</td></tr>  <tr><td>last_week</td><td>Monday 00:00:00 of previous week</td><td>Sunday 23:59:59 of previous week</td><td>yes</td></tr>  <tr><td>this_day</td><td>00:00:00 of current day</td><td>Now</td><td>yes</td></tr>  <tr><td>this_hour</td><td>00:00 of current clock hour</td><td>Now</td><td>yes</td></tr>  <tr><td>this_month</td><td>1st day 00:00:00 of current month</td><td>Now</td><td>yes</td></tr>  <tr><td>this_week</td><td>Monday 00:00:00 of current week</td><td>Now</td><td>yes</td></tr>  <tr><td>last_year</td><td> Jan 1st 00:00:00 of previous year</td><td>Dec 31st 23:59:59 of previous year</td><td>no</td></tr>  <tr><td>this_year or ytd</td><td>Jan 1st  00:00:0 of current year</td><td>Now</td><td>no</td></tr>  <tr><td>total</td><td>Account creation date</td><td>Now</td><td>no</td></tr>  </table> 
slice = 'slice_example' # str | A reducing method which can be applied to the requested duration. A final slice without an optional slice specifier will define a grouping.  Possible Values:  * `channel`: (optional) A given account's sender  * `domain`: (optional) Sending domain  * `rcpt_domain`: (optional) Recieving domain  * `rcpt_isp`: (optional) Receiving ISP     Slices can be chained in a meaningful way – for example:   ```   /last_month/channel/marketing/domain/smtp.com/rcpt_domain?event=complained   ``` would produce an aggregate of complaints for a current account’s channel (sender) called “marketing” which were:   * sent from the registered email domain “smtp.com”, and    * are grouped by receiving domains       The response would look something like:   ```   {“google.com”: {“complained”: 5}, “yahoo.com”: {“complained”:1}, “aol.com”: {“complained”:1}}   ``` 
slice_specifier = 'slice_specifier_example' # str | slice value (smtp.com, sender1)
group_by = 'group_by_example' # str | Define a grouping:  * `channel` - optionally to be followed by a channel ID or name specifier  * `domain`  - optionally to be followed by a registered domain name  * `rcpt_domain` - optionally to be followed by a registered domain name  * `rcpt_isp` - optionally to be followed by a registered domain name 
limit = 56 # int | Maximum number of items to return.
offset = 56 # int | Number of items to skip before returning the results.
end = 'end_example' # str | The ending time. If not specified, defaults to now. RFC 2822 or UNIX epoch format. (optional)
event = 'event_example' # str | Array of any event names for which stats has been requested. (optional)

    try:
        # Return event aggregates for the specified slices and duration. Slices can be chained.
        api_response = api_instance.v4_stats_duration_slice_slice_specifier_group_by_get(start, duration, slice, slice_specifier, group_by, limit, offset, end=end, event=event)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->v4_stats_duration_slice_slice_specifier_group_by_get: %s\n" % e)
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
    api_instance = smtp.StatisticsApi(api_client)
    start = 'start_example' # str | The starting time. Required if the `{duration}` path parameter is not specified. RFC 2822 or UNIX epoch format.
duration = 'duration_example' # str | A standardized shorthand for a known start/end bracket. Duration automatically supersedes start/end values provided as query string parameters. One of either the `{duration}` path parameter or the `start` query parameter must be specified.  <table>  <tr><th>Value</th><th>Start</th><th>End</th><th>Slicable</th></tr>  <tr><td>last_24hrs</td><td>84,400 seconds ago</td><td>Now</td><td>yes</td></tr>  <tr><td>last_30days</td><td>18,144,000 seconds ago</td><td>Now</td><td>yes</td></tr>  <tr><td>last_7days</td><td>604,800 seconds ago</td><td>Now</td><td>yes</td></tr>  <tr><td>last_day</td><td>00:00:00 of the previous day</td><td>23:59:59 of the previous day</td><td>yes</td></tr>  <tr><td>last_hour</td><td>00:00 of the previous hour</td><td>59:59 of the previous hour</td><td>yes</td></tr>  <tr><td>last_month or mtd</td><td>1st day 00:00:00 of previous month</td><td>23:59:59 last day of previous month</td><td>yes</td></tr>  <tr><td>last_week</td><td>Monday 00:00:00 of previous week</td><td>Sunday 23:59:59 of previous week</td><td>yes</td></tr>  <tr><td>this_day</td><td>00:00:00 of current day</td><td>Now</td><td>yes</td></tr>  <tr><td>this_hour</td><td>00:00 of current clock hour</td><td>Now</td><td>yes</td></tr>  <tr><td>this_month</td><td>1st day 00:00:00 of current month</td><td>Now</td><td>yes</td></tr>  <tr><td>this_week</td><td>Monday 00:00:00 of current week</td><td>Now</td><td>yes</td></tr>  <tr><td>last_year</td><td> Jan 1st 00:00:00 of previous year</td><td>Dec 31st 23:59:59 of previous year</td><td>no</td></tr>  <tr><td>this_year or ytd</td><td>Jan 1st  00:00:0 of current year</td><td>Now</td><td>no</td></tr>  <tr><td>total</td><td>Account creation date</td><td>Now</td><td>no</td></tr>  </table> 
slice = 'slice_example' # str | A reducing method which can be applied to the requested duration. A final slice without an optional slice specifier will define a grouping.  Possible Values:  * `channel`: (optional) A given account's sender  * `domain`: (optional) Sending domain  * `rcpt_domain`: (optional) Recieving domain  * `rcpt_isp`: (optional) Receiving ISP     Slices can be chained in a meaningful way – for example:   ```   /last_month/channel/marketing/domain/smtp.com/rcpt_domain?event=complained   ``` would produce an aggregate of complaints for a current account’s channel (sender) called “marketing” which were:   * sent from the registered email domain “smtp.com”, and    * are grouped by receiving domains       The response would look something like:   ```   {“google.com”: {“complained”: 5}, “yahoo.com”: {“complained”:1}, “aol.com”: {“complained”:1}}   ``` 
slice_specifier = 'slice_specifier_example' # str | slice value (smtp.com, sender1)
group_by = 'group_by_example' # str | Define a grouping:  * `channel` - optionally to be followed by a channel ID or name specifier  * `domain`  - optionally to be followed by a registered domain name  * `rcpt_domain` - optionally to be followed by a registered domain name  * `rcpt_isp` - optionally to be followed by a registered domain name 
limit = 56 # int | Maximum number of items to return.
offset = 56 # int | Number of items to skip before returning the results.
end = 'end_example' # str | The ending time. If not specified, defaults to now. RFC 2822 or UNIX epoch format. (optional)
event = 'event_example' # str | Array of any event names for which stats has been requested. (optional)

    try:
        # Return event aggregates for the specified slices and duration. Slices can be chained.
        api_response = api_instance.v4_stats_duration_slice_slice_specifier_group_by_get(start, duration, slice, slice_specifier, group_by, limit, offset, end=end, event=event)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->v4_stats_duration_slice_slice_specifier_group_by_get: %s\n" % e)
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
    api_instance = smtp.StatisticsApi(api_client)
    start = 'start_example' # str | The starting time. Required if the `{duration}` path parameter is not specified. RFC 2822 or UNIX epoch format.
duration = 'duration_example' # str | A standardized shorthand for a known start/end bracket. Duration automatically supersedes start/end values provided as query string parameters. One of either the `{duration}` path parameter or the `start` query parameter must be specified.  <table>  <tr><th>Value</th><th>Start</th><th>End</th><th>Slicable</th></tr>  <tr><td>last_24hrs</td><td>84,400 seconds ago</td><td>Now</td><td>yes</td></tr>  <tr><td>last_30days</td><td>18,144,000 seconds ago</td><td>Now</td><td>yes</td></tr>  <tr><td>last_7days</td><td>604,800 seconds ago</td><td>Now</td><td>yes</td></tr>  <tr><td>last_day</td><td>00:00:00 of the previous day</td><td>23:59:59 of the previous day</td><td>yes</td></tr>  <tr><td>last_hour</td><td>00:00 of the previous hour</td><td>59:59 of the previous hour</td><td>yes</td></tr>  <tr><td>last_month or mtd</td><td>1st day 00:00:00 of previous month</td><td>23:59:59 last day of previous month</td><td>yes</td></tr>  <tr><td>last_week</td><td>Monday 00:00:00 of previous week</td><td>Sunday 23:59:59 of previous week</td><td>yes</td></tr>  <tr><td>this_day</td><td>00:00:00 of current day</td><td>Now</td><td>yes</td></tr>  <tr><td>this_hour</td><td>00:00 of current clock hour</td><td>Now</td><td>yes</td></tr>  <tr><td>this_month</td><td>1st day 00:00:00 of current month</td><td>Now</td><td>yes</td></tr>  <tr><td>this_week</td><td>Monday 00:00:00 of current week</td><td>Now</td><td>yes</td></tr>  <tr><td>last_year</td><td> Jan 1st 00:00:00 of previous year</td><td>Dec 31st 23:59:59 of previous year</td><td>no</td></tr>  <tr><td>this_year or ytd</td><td>Jan 1st  00:00:0 of current year</td><td>Now</td><td>no</td></tr>  <tr><td>total</td><td>Account creation date</td><td>Now</td><td>no</td></tr>  </table> 
slice = 'slice_example' # str | A reducing method which can be applied to the requested duration. A final slice without an optional slice specifier will define a grouping.  Possible Values:  * `channel`: (optional) A given account's sender  * `domain`: (optional) Sending domain  * `rcpt_domain`: (optional) Recieving domain  * `rcpt_isp`: (optional) Receiving ISP     Slices can be chained in a meaningful way – for example:   ```   /last_month/channel/marketing/domain/smtp.com/rcpt_domain?event=complained   ``` would produce an aggregate of complaints for a current account’s channel (sender) called “marketing” which were:   * sent from the registered email domain “smtp.com”, and    * are grouped by receiving domains       The response would look something like:   ```   {“google.com”: {“complained”: 5}, “yahoo.com”: {“complained”:1}, “aol.com”: {“complained”:1}}   ``` 
slice_specifier = 'slice_specifier_example' # str | slice value (smtp.com, sender1)
group_by = 'group_by_example' # str | Define a grouping:  * `channel` - optionally to be followed by a channel ID or name specifier  * `domain`  - optionally to be followed by a registered domain name  * `rcpt_domain` - optionally to be followed by a registered domain name  * `rcpt_isp` - optionally to be followed by a registered domain name 
limit = 56 # int | Maximum number of items to return.
offset = 56 # int | Number of items to skip before returning the results.
end = 'end_example' # str | The ending time. If not specified, defaults to now. RFC 2822 or UNIX epoch format. (optional)
event = 'event_example' # str | Array of any event names for which stats has been requested. (optional)

    try:
        # Return event aggregates for the specified slices and duration. Slices can be chained.
        api_response = api_instance.v4_stats_duration_slice_slice_specifier_group_by_get(start, duration, slice, slice_specifier, group_by, limit, offset, end=end, event=event)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->v4_stats_duration_slice_slice_specifier_group_by_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **str**| The starting time. Required if the &#x60;{duration}&#x60; path parameter is not specified. RFC 2822 or UNIX epoch format. | 
 **duration** | **str**| A standardized shorthand for a known start/end bracket. Duration automatically supersedes start/end values provided as query string parameters. One of either the &#x60;{duration}&#x60; path parameter or the &#x60;start&#x60; query parameter must be specified.  &lt;table&gt;  &lt;tr&gt;&lt;th&gt;Value&lt;/th&gt;&lt;th&gt;Start&lt;/th&gt;&lt;th&gt;End&lt;/th&gt;&lt;th&gt;Slicable&lt;/th&gt;&lt;/tr&gt;  &lt;tr&gt;&lt;td&gt;last_24hrs&lt;/td&gt;&lt;td&gt;84,400 seconds ago&lt;/td&gt;&lt;td&gt;Now&lt;/td&gt;&lt;td&gt;yes&lt;/td&gt;&lt;/tr&gt;  &lt;tr&gt;&lt;td&gt;last_30days&lt;/td&gt;&lt;td&gt;18,144,000 seconds ago&lt;/td&gt;&lt;td&gt;Now&lt;/td&gt;&lt;td&gt;yes&lt;/td&gt;&lt;/tr&gt;  &lt;tr&gt;&lt;td&gt;last_7days&lt;/td&gt;&lt;td&gt;604,800 seconds ago&lt;/td&gt;&lt;td&gt;Now&lt;/td&gt;&lt;td&gt;yes&lt;/td&gt;&lt;/tr&gt;  &lt;tr&gt;&lt;td&gt;last_day&lt;/td&gt;&lt;td&gt;00:00:00 of the previous day&lt;/td&gt;&lt;td&gt;23:59:59 of the previous day&lt;/td&gt;&lt;td&gt;yes&lt;/td&gt;&lt;/tr&gt;  &lt;tr&gt;&lt;td&gt;last_hour&lt;/td&gt;&lt;td&gt;00:00 of the previous hour&lt;/td&gt;&lt;td&gt;59:59 of the previous hour&lt;/td&gt;&lt;td&gt;yes&lt;/td&gt;&lt;/tr&gt;  &lt;tr&gt;&lt;td&gt;last_month or mtd&lt;/td&gt;&lt;td&gt;1st day 00:00:00 of previous month&lt;/td&gt;&lt;td&gt;23:59:59 last day of previous month&lt;/td&gt;&lt;td&gt;yes&lt;/td&gt;&lt;/tr&gt;  &lt;tr&gt;&lt;td&gt;last_week&lt;/td&gt;&lt;td&gt;Monday 00:00:00 of previous week&lt;/td&gt;&lt;td&gt;Sunday 23:59:59 of previous week&lt;/td&gt;&lt;td&gt;yes&lt;/td&gt;&lt;/tr&gt;  &lt;tr&gt;&lt;td&gt;this_day&lt;/td&gt;&lt;td&gt;00:00:00 of current day&lt;/td&gt;&lt;td&gt;Now&lt;/td&gt;&lt;td&gt;yes&lt;/td&gt;&lt;/tr&gt;  &lt;tr&gt;&lt;td&gt;this_hour&lt;/td&gt;&lt;td&gt;00:00 of current clock hour&lt;/td&gt;&lt;td&gt;Now&lt;/td&gt;&lt;td&gt;yes&lt;/td&gt;&lt;/tr&gt;  &lt;tr&gt;&lt;td&gt;this_month&lt;/td&gt;&lt;td&gt;1st day 00:00:00 of current month&lt;/td&gt;&lt;td&gt;Now&lt;/td&gt;&lt;td&gt;yes&lt;/td&gt;&lt;/tr&gt;  &lt;tr&gt;&lt;td&gt;this_week&lt;/td&gt;&lt;td&gt;Monday 00:00:00 of current week&lt;/td&gt;&lt;td&gt;Now&lt;/td&gt;&lt;td&gt;yes&lt;/td&gt;&lt;/tr&gt;  &lt;tr&gt;&lt;td&gt;last_year&lt;/td&gt;&lt;td&gt; Jan 1st 00:00:00 of previous year&lt;/td&gt;&lt;td&gt;Dec 31st 23:59:59 of previous year&lt;/td&gt;&lt;td&gt;no&lt;/td&gt;&lt;/tr&gt;  &lt;tr&gt;&lt;td&gt;this_year or ytd&lt;/td&gt;&lt;td&gt;Jan 1st  00:00:0 of current year&lt;/td&gt;&lt;td&gt;Now&lt;/td&gt;&lt;td&gt;no&lt;/td&gt;&lt;/tr&gt;  &lt;tr&gt;&lt;td&gt;total&lt;/td&gt;&lt;td&gt;Account creation date&lt;/td&gt;&lt;td&gt;Now&lt;/td&gt;&lt;td&gt;no&lt;/td&gt;&lt;/tr&gt;  &lt;/table&gt;  | 
 **slice** | **str**| A reducing method which can be applied to the requested duration. A final slice without an optional slice specifier will define a grouping.  Possible Values:  * &#x60;channel&#x60;: (optional) A given account&#39;s sender  * &#x60;domain&#x60;: (optional) Sending domain  * &#x60;rcpt_domain&#x60;: (optional) Recieving domain  * &#x60;rcpt_isp&#x60;: (optional) Receiving ISP     Slices can be chained in a meaningful way – for example:   &#x60;&#x60;&#x60;   /last_month/channel/marketing/domain/smtp.com/rcpt_domain?event&#x3D;complained   &#x60;&#x60;&#x60; would produce an aggregate of complaints for a current account’s channel (sender) called “marketing” which were:   * sent from the registered email domain “smtp.com”, and    * are grouped by receiving domains       The response would look something like:   &#x60;&#x60;&#x60;   {“google.com”: {“complained”: 5}, “yahoo.com”: {“complained”:1}, “aol.com”: {“complained”:1}}   &#x60;&#x60;&#x60;  | 
 **slice_specifier** | **str**| slice value (smtp.com, sender1) | 
 **group_by** | **str**| Define a grouping:  * &#x60;channel&#x60; - optionally to be followed by a channel ID or name specifier  * &#x60;domain&#x60;  - optionally to be followed by a registered domain name  * &#x60;rcpt_domain&#x60; - optionally to be followed by a registered domain name  * &#x60;rcpt_isp&#x60; - optionally to be followed by a registered domain name  | 
 **limit** | **int**| Maximum number of items to return. | 
 **offset** | **int**| Number of items to skip before returning the results. | 
 **end** | **str**| The ending time. If not specified, defaults to now. RFC 2822 or UNIX epoch format. | [optional] 
 **event** | **str**| Array of any event names for which stats has been requested. | [optional] 

### Return type

[**StatsResponse**](StatsResponse.md)

### Authorization

[apiID](../README.md#apiID), [apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get stats |  -  |
**400** | Query or path params invalid |  -  |
**401** | Invalid API Key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

