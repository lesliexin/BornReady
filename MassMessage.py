from twilio import twiml
from twilio.rest import TwilioRestClient

numArray = ["6474619074","4165581768","6478651824","4168828085"]

ACCOUNT_SID = "ACa7cdb4f507932115a687442f2ac6ccae"
AUTH_TOKEN = "f29b03fe26c7f32805a829614a0f50f2"
    
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

for i in range (0,4):
    client.messages.create(
        to = "+1" + numArray[i],
        from_ = "+16475591787",
        #Example of mass message to send 
        body= "Hey there! It's Leslie from Born Ready. Just wanted to let you know that morning sickness may occur during your current stage of pregnancy. Don't be alarmed if you feel nauseous, bloated or fatigued.",

        #Possibility of using mms in future applications 
        #media_url="https://www.flickr.com/photos/145193312@N04/shares/907B87",
    )

