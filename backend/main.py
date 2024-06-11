from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/log-in', methods=['POST'])
def log_in():
    try:
        # Hacer una solicitud GET al servicio de reservas
        response = requests.post(f"log-in-service:8080/log_in", json=request.json)
        return jsonify(response.json()), response.status_code

    except Exception as e:
        return jsonify({"message": f"Error: {e}"}), response.status_code

@app.route('/make-admin', methods=['POST'])
def make_admin():
    try:
        # Hacer una solicitud GET al servicio de reservas
        admin_response = requests.get(f"validate-token-service:8080/is_admin") # Asumiendo que tambien valida token valid
        if admin_response.status_code == 200:
            response = requests.post(f"make-admin-service:8080/make_admin", json=request.json)
            return jsonify(response.json()), response.status_code

    except Exception as e:
        return jsonify({"message": f"Error: {e}"}), response.status_code

@app.route('/get-menu', methods=['GET'])
def get_menu():
    try:
        
        #token_response = requests.get(f"validate-token-service:8080/is_token_valid")
        #if token_response.status_code == 200:
        response = requests.get("http://menu-service:8080/get_menu")
        response.raise_for_status()  # Raise exception for non-200 status codes
        return jsonify(response.json()), response.status_code, {'Access-Control-Allow-Origin': '*'}
        #else: # invalid token
         #   return jsonify(token_response.json()), token_response.status_code, {'Access-Control-Allow-Origin': '*'}

    except requests.exceptions.RequestException as e:
        return jsonify({"message": f"Error: {e}"}), response.status_code, {}  # Internal Server Error


@app.route('/get-recommendation', methods=['POST'])
def get_recommendation():
    try:
        # Hacer una solicitud POST al servicio de Sentiment Analysis
        token_response = requests.get(f"validate-token-service:8080/is_token_valid")
        if token_response.status_code == 200:
            response = requests.post(f"recommendation-service:8080/recomendations", json=request.json)
            return jsonify(response.json()), response.status_code, {'Access-Control-Allow-Origin': '*'}
        else: # invalid token
            return jsonify(token_response.json()), token_response.status_code, {'Access-Control-Allow-Origin': '*'}
    except Exception as e:
        return jsonify({"message": f"Error: {e}"}), response.status_code

@app.route('/reset-password', methods=['POST'])
def reset_password():
    try:
        # Hacer una solicitud GET al servicio de reset password
        token_response = requests.get(f"validate-token-service:8080/is_token_valid")
        if token_response.status_code == 200:
            response = requests.post(f"validate-token-service:8080/reset_password", json=request.json)
            return jsonify(response.json()), response.status_code
        else: # invalid token
            return jsonify(token_response.json()), token_response.status_code, {'Access-Control-Allow-Origin': '*'}
    except Exception as e:
        return jsonify({"message": f"Error: {e}"}), response.status_code

@app.route('/sign-up', methods=['POST'])
def sign_up():
    try:
        # Hacer una solicitud GET al servicio de reservas
        response = requests.post(f"sign-up-service:8080/sign_up", json=request.json)
        return jsonify(response.json()), response.status_code, {'Access-Control-Allow-Origin': '*'}

    except Exception as e:
        return jsonify({"message": f"Error: {e}"}), response.status_code

@app.route('/create-reservation', methods=['POST'])
def create_reservation():
    try:
        # Hacer una solicitud GET al servicio de reservas
        token_response = requests.get(f"validate-token-service:8080/is_token_valid")
        if token_response.status_code == 200:
            response = requests.post(f"reservation-service:8080/create_reservation", json=request.json)
            return jsonify(response.json()), response.status_code

    except Exception as e:
        return jsonify({"message": f"Error: {e}"}), response.status_code


@app.route('/get-reservation', methods=['GET'])
def get_reservation():
    try:
        # Hacer una solicitud GET al servicio de reservas
        token_response = requests.get(f"validate-token-service:8080/is_token_valid")
        if token_response.status_code == 200:
            response = requests.get(f"reservation-service:8080/create_reservation")
            return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"message": f"Error: {e}"}), response.status_code

@app.route('/update-reservation', methods=['PUT'])
def update_reservation():
    try:
        # Hacer una solicitud GET al servicio de reservas
        token_response = requests.get(f"validate-token-service:8080/is_token_valid")
        if token_response.status_code == 200:
            response = requests.put(f"reservation-service:8080/create_reservation", json=request.json)
            return jsonify(response.json()), response.status_code

    except Exception as e:
        return jsonify({"message": f"Error: {e}"}), response.status_code

@app.route('/delete-reservation', methods=['DELETE'])
def delete_reservation():
    try:
        # Hacer una solicitud GET al servicio de reservas
        token_response = requests.get(f"validate-token-service:8080/is_token_valid")
        if token_response.status_code == 200:
            response = requests.delete(f"reservation-service:8080/create_reservation", json=request.json)
            return jsonify(response.json()), response.status_code

    except Exception as e:
        return jsonify({"message": f"Error: {e}"}), response.status_code



@app.route('/')
def index():
    return 'Welcome to the MYRESTaurant Reservation System!'

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=8080)