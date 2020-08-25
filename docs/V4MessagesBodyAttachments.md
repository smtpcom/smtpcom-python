# V4MessagesBodyAttachments

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | MIME version. By default set to &#x60;1.0&#x60; | [optional] 
**type** | **str** | MIME type. By default set to &#x60;application/octet-stream&#x60; | [optional] 
**disposition** | **str** | Content-disposition, either &#x60;inline&#x60; or &#x60;attachment&#x60;. By default set to &#x60;attachment&#x60; | [optional] 
**filename** | **str** | Name of attached file | [optional] 
**cid** | **str** | Content ID for inline dispositions. By default this is equal to the filename. Can be used in HTML content to address an attached image using “cid:” URL scheme. | [optional] 
**content** | **str** | Actual attachment content in its raw form | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


