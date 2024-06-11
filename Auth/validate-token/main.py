from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials
from firebase_admin import firestore
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Allow CORS for all domains

cred = credentials.Certificate('firebase_admin_sdk_credentials.json')
firebase_admin.initialize_app(cred)
db = firestore.client()


@app.route('/is_token_valid', methods=['GET'])
def is_token_valid():
    try:
        token = request.headers['Authorization']
        if (validate_and_decode_token(token)):
            return jsonify({"Success": "Token is valid"}), 200
        else:
            return jsonify({"Error": "Token is invalid"}), 401
    except Exception as e:
        return handle_error(e)

@app.route('/is_admin', methods=['GET'])
def is_admin():
    try:
        token = request.headers['Authorization']
        decoded_token = validate_and_decode_token(token)
        if (is_token_admin(decoded_token)):
            return jsonify({"Success": "User is an admin"}), 200
        else:
            raise Exception("User is not an admin")
    except Exception as e:
        return handle_error(e)

def is_token_admin(decoded_token):
    isAdmin = decoded_token["isAdmin"]
    if isAdmin:
        return True
    else:
        return False

def validate_and_decode_token(token):
    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token
    except:
        raise Exception("Invalid token")

def handle_error(e):
    if str(e) == "Invalid token":
        return jsonify({"Error": "Invalid Token"}), 401
    elif str(e) == "User is not an admin":
        return jsonify({"Error": "User is not an admin"}), 401
    else:
        return jsonify({"Error": str(e), "Type": str(type(e))}), 500  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
