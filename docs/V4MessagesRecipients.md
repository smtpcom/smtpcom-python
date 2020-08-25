# V4MessagesRecipients

At least one of `to`, `cc`, `bcc` or `bulk_list` must be specified here. `bulk_list` can not be used with `to`, `cc` or `bcc` 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | [**list[V4MessagesRecipientsTo]**](V4MessagesRecipientsTo.md) | TO recipients list | [optional] 
**cc** | [**list[V4MessagesRecipientsTo]**](V4MessagesRecipientsTo.md) | CC recipients list | [optional] 
**bcc** | [**list[V4MessagesRecipientsTo]**](V4MessagesRecipientsTo.md) | BCC recipients list | [optional] 
**bulk_list** | [**list[V4MessagesRecipientsTo]**](V4MessagesRecipientsTo.md) | Distribution list. Instead of an individual email to multiple recipients, multiple emails to multiple recipients will be created. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


