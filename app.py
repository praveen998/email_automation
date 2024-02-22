# app.py

from flask import Flask
#from automation2 import send_email
from database import DatabaseConnection

app = Flask(__name__)

@app.route('/conn')
def index():
    return 'hello'

@app.route('/sendmail')
def sendmail():
   
    your_email = "praveen.gopi717@gmail.com"
    your_password = "wsjb dise wtad bspn"
    message = "new message 1"

    return (send_email(your_email, your_password, message))
@app.route('/')
def conn():
     client=DatabaseConnection()
     client=client.get_client()
     db=client['post']

     # Accessing a specific collection within the database
     collection = db['jobs']
     doc=collection.find()

     print("All documents in the collection:")
     for document in doc:
         print(document)
     client.close()

     return 'success'

if __name__ == '__main__':
    app.run(debug=True)
