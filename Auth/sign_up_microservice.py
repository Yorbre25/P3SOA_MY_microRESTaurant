from flask import Flask, request, jsonify
from firebase_credentials import firebase_config
import pyrebase
import requests

app = Flask(__name__)

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

# Todo: Check if user already exists
def handle_error(e):
    if isinstance(e, requests.HTTPError):
        return {"Error": "Invalid Login Credentials"}, 400
    else:
        return jsonify({"Error": str(e), "Type": str(type(e))}), 500
    

@app.route('/sign_up', methods=['POST'])
def sign_up():
    data = request.json
    email = data['email']
    password = data['password']
    try: 
        user = auth.create_user_with_email_and_password(email=email, password=password)
        return jsonify(user), 200
    except Exception as e:
        return handle_error(e)
        

if __name__ == '__main__':
    app.run(debug=True)







