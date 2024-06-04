from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials
from firebase_admin import firestore

app = Flask(__name__)

# todo: Check for admin attribute in jwt

cred = credentials.Certificate('Auth/firebase_admin_sdk_credentials.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

def handle_error(e):
    if isinstance(e, firebase_admin._auth_utils.UserNotFoundError):
        return jsonify({"Error": "User not found"}), 400
    else:
        return jsonify({"Error": str(e), "Type": str(type(e))}), 500

def make_admin_with_firebase(user_id):
    custom_claim = {
        'isAdmin': True
    }
    auth.set_custom_user_claims(user_id, custom_claim)
    
@app.route('/make_admin', methods=['POST'])
def make_admin():
    try:
        data = request.json
        user_id = data['user_id']
        make_admin_with_firebase(user_id)
        return jsonify({"Success": "User is now an admin"}), 200
    except Exception as e:
        return handle_error(e)


if __name__ == '__main__':
    app.run(debug=True)
