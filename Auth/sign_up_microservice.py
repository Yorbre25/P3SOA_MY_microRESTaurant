from flask import Flask, request, jsonify
from firebase_credentials import firebase_config
import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials
from firebase_admin import firestore
import pyrebase
import requests

app = Flask(__name__)

# Init Firebase SDK to create user
firebase = pyrebase.initialize_app(firebase_config)
authentification = firebase.auth()

# Init Firebase Admin SDK to user firestore
cred = credentials.Certificate('Auth/firebase_admin_sdk_credentials.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route('/sign_up', methods=['POST'])
def sign_up():
    try: 
        data = request.json
        name = data['name']
        email = data['email']
        password = data['password']
        user = sign_up_with_firebase(email, password)
        add_data(email, name, user['localId'])
        return jsonify(user), 200
    except Exception as e:
        return handle_error(e)

def sign_up_with_firebase(email, password):
    user = authentification.create_user_with_email_and_password(email=email, password=password)
    add_custom_claim = {
        'isAdmin': False
    }
    auth.set_custom_user_claims(user["localId"], add_custom_claim)
    return authentification.sign_in_with_email_and_password(email=email, password=password)

def add_data(email, name, user_id):
    doc_ref = db.collection('users').document(email)
    doc_ref.set({
        'name': name,
        "email": email,
        "user_id": user_id
    })

def handle_error(e):
    if isinstance(e, requests.HTTPError):
        return {"Error": "Invalid Login Credentials"}, 400
    else:
        return jsonify({"Error": str(e), "Type": str(type(e))}), 500
    




if __name__ == '__main__':
    app.run(debug=True)







