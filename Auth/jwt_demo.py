from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials

"""
Esto es una demo de como verificar un JWT con firebase. 
La vara funciona así, el JWT se agrega al header "Authorization" de las request.
En el jwt viene info del usuario cifrada, firebase tiene una llave para descifrarlo.
"""

"""
Primero se inicializa la app de firebase con las credenciales. 
Este archivo no está en el repo por razones de seguridad. Lo mandé por WhatsApp.
"""
cred = credentials.Certificate("Auth/firebase_admin_sdk_credentials.json")
firebase_admin.initialize_app(cred)

app = Flask(__name__)

@app.route('/', methods=['POST'])
def demo():
    token = request.headers['Authorization'] # Se obtiene el JWT del header
    decoded_token = auth.verify_id_token(token) # Se verifica el JWT. Si no es válido, se lanza una excepción.
    #Un vez decifrado podemos leer la info del usuario.
    #Los atributos como si es admin ahora se pueden leer
    print(decoded_token)
    return jsonify({"message": "Todo salió bien"}), 200


if __name__ == '__main__':
    app.run(debug=True)
