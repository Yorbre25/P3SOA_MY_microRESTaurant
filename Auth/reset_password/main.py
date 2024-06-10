from flask import Flask, request, jsonify
from firebase_credentials import firebase_config
import pyrebase
import requests

app = Flask(__name__)

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

def handle_error(e):
    if isinstance(e, requests.HTTPError):
        return {"Error": "Invalid Email"}, 400
    else:
        return jsonify({"Error": str(e), "Type": str(type(e))}), 500
    

@app.route('/reset_password', methods=['POST'])
def sign_up():
    data = request.json
    email = data['email']
    try: 
        auth.send_password_reset_email(email)
        return {"Message":"Correo Enviado"},200
    except Exception as e:
        return handle_error(e)
        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)