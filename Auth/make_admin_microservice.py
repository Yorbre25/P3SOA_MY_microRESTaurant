from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

app = Flask(__name__)

cred = credentials.Certificate('Auth/firebase_admin_sdk_credentials.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

def handle_error(e):
    if isinstance(e, Exception):
        return jsonify({"Error": "User not found"}), 400
    else:
        return jsonify({"Error": str(e), "Type": str(type(e))}), 500
    

def make_admin_with_firebase(email):
    doc_ref = db.collection("users").document(email)
    doc = doc_ref.get()

    if doc.exists:
        doc_ref.update({
            'isAdmin': True
        })
    else:
        raise Exception("User not found")

@app.route('/make_admin', methods=['POST'])
def make_admin():
    try:
        data = request.json
        email = data['email']
        make_admin_with_firebase(email)
        return jsonify({"Success": "User is now an admin"}), 200
    except Exception as e:
        return handle_error(e)


if __name__ == '__main__':
    app.run(debug=True)
