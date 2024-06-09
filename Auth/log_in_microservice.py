from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pyrebase
import requests

from firebase_credentials import firebase_config

app = Flask(__name__)

# Init Firebase SDK to create user
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

# Init Firebase Admin SDK to user firestore
cred = credentials.Certificate('Auth/firebase_admin_sdk_credentials.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

def handle_error(e):
    if isinstance(e, requests.exceptions.HTTPError):
        return jsonify({"Error": "Invalid Login Credentials"}), 400
    else:
        return jsonify({"Error": str(e), "Type": str(type(e))}), 500

def log_in_with_firebase(email, password):
    return auth.sign_in_with_email_and_password(email=email, password=password)

def get_user_data(email):
    doc_ref = db.collection('users').document(email)
    doc = doc_ref.get()
    return doc.to_dict()

def append_user_data(user, email):
    data = get_user_data(email)
    user["displayName"] = data["name"]
    return user
    
    
@app.route('/log_in', methods=['POST'])
def log_in():
    try: 
        data = request.json
        email = data['email']
        password = data['password']
        
        user = log_in_with_firebase(email, password)
        user = append_user_data(user, email)
        return jsonify(user), 200
    except Exception as e:
        return handle_error(e)
    

if __name__ == '__main__':
    app.run(debug=True)
