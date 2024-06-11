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

@app.route('/make_admin', methods=['POST'])
def make_admin():
    try:
        token = request.headers['Authorization']
        if (is_request_valid(token)):
            data = request.json
            email = data['email']
            make_admin_with_firebase(email)
            return jsonify({"Success": "User is now an admin"}), 200
        else:
            raise Exception("Unauthorized")
    except Exception as e:
        return handle_error(e)

def is_request_valid(token):
    decoded_token = validate_and_decode_token(token)
    return is_admin(decoded_token)

def validate_and_decode_token(token):
    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token
    except:
        raise Exception("Invalid token")

def is_admin(decoded_token):
    print(decoded_token)
    isAdmin = decoded_token["isAdmin"]
    if isAdmin:
        return True
    else:
        raise Exception("Unauthorized")
    
def make_admin_with_firebase(email):
    user = auth.get_user_by_email(email)
    print(type(user))
    custom_claim = {
        'isAdmin': True
    }
    auth.set_custom_user_claims(user.uid, custom_claim)
    
def handle_error(e):
    # if isinstance(e, firebase_admin._auth_utils.UserNotFoundError):
    #     return jsonify({"Error": "User not found"}), 400
    # elif str(e) == "Invalid token":
    #     return jsonify({"Error": "Invalid Token"}), 401
    # elif str(e) == "Unauthorized":
    #     return jsonify({"Error": "Unauthorized"}), 401
    # else:
        return jsonify({"Error": str(e), "Type": str(type(e))}), 500    



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
