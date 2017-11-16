import pyrebase

config = {
    "apiKey": "AIzaSyAJopo0jp7WgykhF67K37jp0003qysmX_Y",
    "authDomain": "innovationsmartoffice.firebaseapp.com",
    "databaseURL": "https://innovationsmartoffice.firebaseio.com",
    "storageBucket": "innovationsmartoffice.appspot.com",
}
FIREBASE_EMAIL = 'innovation080917@gmail.com'

firebase = pyrebase.initialize_app(config)
#auth = firebase.auth()

#authenticate a user
#user = auth.sign_in_with_email_and_password(FIREBASE_EMAIL, "innovation080917")
def stream_handler(message):
	print(message) # put
	#print(message["pin_number"]) # /-K7yGTTEp7O549EzTYtI
	#print(message["switch_number"]) # {'title': 'Pyrebase', "body": "etc..."}

db = firebase.database()

my_stream = db.child("controls").stream(stream_handler)