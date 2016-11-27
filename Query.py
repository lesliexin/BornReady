from flask import Flask, request, redirect
from twilio import twiml

app = Flask(__name__)

@app.route("/sms", methods=['GET','POST'])

def incoming_sms():
    #Send a dynamic reply to an incoming text message
 
    resp = twiml.Response()

    #Get the message the user sent our Twilio number
    
    message = request.values.get('Body', None)

    person ="leslie xin, mississauga, 3, 4, +16478651824"

    resp.message(person)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
