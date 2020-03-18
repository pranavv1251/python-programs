from twilio.rest import Client

account_sid = '<Account SID>'
auth_token = '<Authorization Token>'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+12077394223',
    to='+919689558750',
    body='This is a system message!'
)

print(message.sid)
