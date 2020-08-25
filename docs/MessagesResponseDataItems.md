# MessagesResponseDataItems

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**msg_id** | **str** | Unique message ID | [optional] 
**msg_time** | **int** | Time at which the message was sent | [optional] 
**channel** | **str** | Name of the channel on which the message was sent | [optional] 
**smtp_vars** | **object** | Custom parameters and their value echoed back from &#x60;X-SMTPAPI&#x60; header&#39;s &#x60;unique_args&#x60; parameter | [optional] 
**msg_data** | [**MessagesResponseDataMsgData**](MessagesResponseDataMsgData.md) |  | [optional] 
**details** | [**MessagesResponseDataDetails**](MessagesResponseDataDetails.md) |  | [optional] 
**opens** | [**MessagesResponseDataOpens**](MessagesResponseDataOpens.md) |  | [optional] 
**clicks** | [**MessagesResponseDataClicks**](MessagesResponseDataClicks.md) |  | [optional] 
**abuse** | [**MessagesResponseDataAbuse**](MessagesResponseDataAbuse.md) |  | [optional] 
**unsubs** | [**MessagesResponseDataUnsubs**](MessagesResponseDataUnsubs.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


