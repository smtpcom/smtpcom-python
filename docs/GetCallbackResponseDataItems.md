# GetCallbackResponseDataItems

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**medium** | **str** | Medium by which the callback data is sent. Possible values are one of:   * http   * aws  | [optional] 
**event** | **str** | Event for which the callback has been created. Valid types are:  * delivered -  message delivered * failed - message bounced * complained - complaint received * bounceback - bounce back notification received * received - message received by our system * queued - message in queue (transient) * hard_bounced - hard bounce received * opened - message opened * clicked - URL in message clicked * unsubscribed - unsubscribe received  | [optional] 
**channel** | **str** | Name of the channel for which the callback has been created | [optional] 
**address** | **str** | Address to which the callback data is sent. This will be either a URL for http-based callbacks or the Amazon SQS queue name for SQS-based callbacks | [optional] 
**aws_data** | **str** | Amazon SQS settings | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


