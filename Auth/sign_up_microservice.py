from flask import Flask, request, jsonify
from firebase_credentials import firebase_config
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pyrebase
import requests

app = Flask(__name__)

# Init Firebase SDK to create user
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

# Init Firebase Admin SDK to user firestore
cred = credentials.Certificate('Auth/firebase_admin_sdk_credentials.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

# Todo: Check if user already exists
def handle_error(e):
    if isinstance(e, requests.HTTPError):
        return {"Error": "Invalid Login Credentials"}, 400
    else:
        return jsonify({"Error": str(e), "Type": str(type(e))}), 500
    

def add_data(email, name):
    doc_ref = db.collection('users').document(email)
    doc_ref.set({
        'name': name,
        'isAdmin': False
    })

def sign_up_with_firebase(email, password):
    return auth.create_user_with_email_and_password(email=email, password=password)

@app.route('/sign_up', methods=['POST'])
def sign_up():
    try: 
        data = request.json
        name = data['name']
        email = data['email']
        password = data['password']
        user = sign_up_with_firebase(email, password)
        add_data(email, name)
        return jsonify(user), 200
    except Exception as e:
        return handle_error(e)
        

if __name__ == '__main__':
    app.run(debug=True)







