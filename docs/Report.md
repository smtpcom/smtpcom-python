# Report

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency** | **str** | Report frequency – one of:   * daily - every day at a specified hour   * weekly - Mondays at a specified hour   * monthly - 1st day of the month at a specified hour  | [optional] 
**report_id** | **str** | Unique report ID | [optional] 
**events** | **str** | Preset of events returned in a report:    * hard_bounced   * failed   * delivered   * sent   * pending   * total   * abuse If not specified all events are included.  | [optional] 
**channel** | **str** | Name of channel (sender). If not specified all channels will be reported | [optional] 
**report_time** | **str** | The hour at which the report should be sent, values range from 0 to 23 | [optional] 
**status** | **str** | Current status of a given on-demand report | [optional] 
**name** | **str** | Human readable name of an on-demand report (auto-generated) | [optional] 
**url** | **str** | The unique URL from which to download an on-demand report from | [optional] 
**time_req** | **int** | Time when a given on-demand report has been requestedi. RFC 2822 or UNIX epoch format | [optional] 
**progress** | **int** | Percentage of completion for an on-demand report | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


