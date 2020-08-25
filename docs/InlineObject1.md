# InlineObject1

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mime** | **str** | A completely prepared full MIME container of the email, compliant with RFC 2045, RFC 2046, RFC 2047, RFC 4288, RFC 4289 and RFC 2049. No validation will be performed during API submission and it will be attempted to be delivered as is. Any errors while processing and delivering this email will be available only via callbacks.   | [optional] 
**channel** | **str** | Name of the channel through which the email will be sent. | [optional] 
**recipients** | [**V4MessagesMimeRecipients**](V4MessagesMimeRecipients.md) |  | [optional] 
**originator** | [**V4MessagesOriginator**](V4MessagesOriginator.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


