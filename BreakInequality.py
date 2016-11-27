from flask import Flask, request, redirect
from twilio import twiml
from twilio.rest import TwilioRestClient

app = Flask(__name__)

@app.route("/sms", methods=['GET','POST'])

def incoming_sms():
    #Send a dynamic reply to an incoming text message
 
    resp = twiml.Response()

    #Get the message the user sent our Twilio number
    
    message = request.values.get('Body', None)

    #Split the array into 5 strings
    
    myArray = message.split(",")

    name = myArray[0]
    location = myArray[1]
    date = int(myArray[2])
    month = int(myArray[3])
    num = int(myArray[4])

    #String to give range of delivery date
    
    c_String = "" 

    #Calculating Delivery date 

    conception = (month+10)%12

    if (date < 11):
        c_String = "Early " 
        
    elif (10<date<21):
        c_String = "Mid " 

    elif (20<date<32):
        c_String += "Late "

    #Converting delivery date from number to string

    allMonths = ["January", "February", "March", "April","May","June","July","August","September","October","November","December"] 

    for i in range (0,11):
        if (conception == i):
            c_String += allMonths[i]

    #Using REST Api to sms woman with projected delivery date
    
    ACCOUNT_SID = "ACa7cdb4f507932115a687442f2ac6ccae"
    AUTH_TOKEN = "f29b03fe26c7f32805a829614a0f50f2"
    
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    
    client.messages.create(
        to = num,
        from_ = "+16475591787",
        body="Your projected date of delivery is: " + c_String
    )

    # Thank the collector for entry
    
    resp.message("Thank you for your entry!")

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
