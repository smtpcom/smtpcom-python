from pprint import pprint

import smtpcom
from smtpcom import ApiException, V4MessagesRecipients, V4MessagesRecipientsTo, V4MessagesOriginator, \
    V4MessagesBody, V4MessagesBodyParts


test_email = 'your_email'
test_api_key = 'your_api_key'
test_sender = 'your_sender_label'


configuration = smtpcom.Configuration(
    api_key={
        'apiKey': test_api_key
    }
)

# Enter a context with an instance of the API client
with smtpcom.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = smtpcom.MessagesApi(api_client)

    recipients = V4MessagesRecipients(to=[V4MessagesRecipientsTo(name='test', address=test_email)])
    originator = V4MessagesOriginator(_from=V4MessagesRecipientsTo(name='test', address=test_email))
    body = V4MessagesBody(parts=[V4MessagesBodyParts(content='Hello')])
    channel = test_sender  # Sender Label
    inline_object = smtpcom.InlineObject(
        recipients=recipients,
        originator=originator,
        subject='Test',
        body=body,
        channel=channel
    )
    try:
        # Send a Message
        api_response = api_instance.v4_messages_post(inline_object=inline_object)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MessagesApi->v4_messages_post: %s\n" % e)
