# MessagesResponseDataDetailsDelivery

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**finished** | **str** | Timestamp of when the message was delivered | [optional] 
**retries** | **int** | Number of retries after the initial delivery attempt | [optional] 
**event** | **str** | One of:    * delivered   * failed   * queued  | [optional] 
**code** | **str** | The last SMTP response code received from a peer | [optional] 
**status** | **str** | The last SMTP response message received from a peer | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


