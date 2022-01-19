# pip3 install twilio

# Download the helper library from https://www.twilio.com/docs/python/install
# import os
# from twilio.rest import Client


# # Find your Account SID and Auth Token at twilio.com/console
# # and set the environment variables. See http://twil.io/secure
# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTHENTICATION_TOKEN']
# client = Client(account_sid, auth_token)

# message = client.messages \
#                 .create(
#                      body="The Message to be sent",
#                      from_='Your number with proper prefix',
#                      to='Receiver\'s number'
#                  )

# print(message.sid)