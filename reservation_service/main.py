import functions_framework
from flask import Flask, jsonify, request
from pydantic import BaseModel, ValidationError
from flask_cors import CORS


app = Flask(__name__)  # Definir la aplicación Flask
CORS(app)

# Simulación de base de datos
reservations_db = []

class Reservation(BaseModel):
    id: int
    user_id: int
    location: str
    time: str
    guests: int

@functions_framework.errorhandler(AssertionError)
def handle_assertion_error(e):
    return jsonify({"msg": "Method not allowed"}), 405, {'Access-Control-Allow-Origin': '*'}

@functions_framework.errorhandler(KeyError)
def handle_key_error(e):
    return jsonify({"msg": "Bad request, missing required fields"}), 400, {'Access-Control-Allow-Origin': '*'}

@functions_framework.errorhandler(ValidationError)
def handle_validation_error(e):
    return jsonify({"msg": "Bad request, validation error"}), 400, {'Access-Control-Allow-Origin': '*'}

@functions_framework.errorhandler(ValueError)
def handle_value_error(e):
    return jsonify({"msg": str(e)}), 400, {'Access-Control-Allow-Origin': '*'}

@functions_framework.errorhandler(TypeError)
def handle_type_error(e):
    return jsonify({"msg": "Type error"}), 400, {'Access-Control-Allow-Origin': '*'}

@functions_framework.http
def create_reservation(request):
    global reservations_db  # Mover la declaración global aquí

    if request.method == "POST":
        if request.is_json:
            data = request.get_json()
            reservation = Reservation(**data)
            reservations_db.append(reservation.dict())
            return jsonify(reservation.dict()), 201, {'Access-Control-Allow-Origin': '*'}
        else:
            raise TypeError("Unsupported Media Type, Content-Type must be application/json")
    elif request.method == "GET":
        user_id = request.args.get('user_id')
        if user_id:
            user_reservations = [res for res in reservations_db if res['user_id'] == int(user_id)]
            return jsonify(user_reservations), 200, {'Access-Control-Allow-Origin': '*'}
        return jsonify(reservations_db)
    elif request.method == "PUT":
        if request.is_json:
            data = request.get_json()
            for reservation in reservations_db:
                if reservation['id'] == data['id']:
                    reservation.update(data)
                    return jsonify(reservation), 200, {'Access-Control-Allow-Origin': '*'}
            return jsonify({"msg": "Reservation not found"}), 404
        else:
            raise TypeError("Unsupported Media Type, Content-Type must be application/json")
    elif request.method == "DELETE":
        if request.is_json:
            data = request.get_json()
            reservations_db = [reservation for reservation in reservations_db if reservation['id'] != data['id']]
            return '', 204, {'Access-Control-Allow-Origin': '*'}
        else:
            raise TypeError("Unsupported Media Type, Content-Type must be application/json")
    else:
        return jsonify({"msg": "Method not allowed"}), 405, {'Access-Control-Allow-Origin': '*'}

@app.route('/<path:path>', methods=['GET'])
def catch_all(path):
    return "Unsupported Media Type. This endpoint only supports application/json.", 415, {'Access-Control-Allow-Origin': '*'}

# Alias para compatibilidad con el framework de funciones
manage_reservations = create_reservation

# Ruta para la función principal
@app.route('/reservations', methods=['GET', 'POST', 'PUT', 'DELETE'])
def reservations():
    return manage_reservations(request)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
