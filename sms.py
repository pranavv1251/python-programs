# Phone Number:-  +12077394223
from twilio.rest import Client

account_sid = 'AC568cdbe940e071258c338a38057b892e'
auth_token = '7e93cf42e513c830e279099b4cf79455'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+12077394223',
    body='Happy Birthday!',
    to='+919689558750'
)

print(message.sid)
