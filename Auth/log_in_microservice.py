from flask import Flask, request, jsonify
from firebase_credentials import firebase_config
import pyrebase
import requests

app = Flask(__name__)


firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

def handle_error(e):
    if isinstance(e, requests.exceptions.HTTPError):
        return jsonify({"Error": "Invalid Login Credentials"}), 400
    else:
        return jsonify({"Error": str(e), "Type": str(type(e))}), 500
    

@app.route('/log_in', methods=['POST'])
def log_in():
    data = request.json
    email = data['email']
    password = data['password']
    user = None
    try: 
        user = auth.sign_in_with_email_and_password(email=email, password=password)
        return jsonify(user), 200
    except Exception as e:
        return handle_error(e)
    

if __name__ == '__main__':
    app.run(debug=True)
