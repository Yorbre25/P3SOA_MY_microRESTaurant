import firebase_admin
from firebase_admin import auth, credentials

# Ruta al archivo JSON de configuración descargado desde Firebase
CREDENTIALS_FILE = "Credentials/firebase_credentials.json"

# Inicializa la aplicación de Firebase con tus credenciales
cred = credentials.Certificate(CREDENTIALS_FILE)
firebase_admin.initialize_app(cred)

def sign_in_with_email_and_password(email, password):
    user = auth.create_user(email=email, password=password)
    return "Usuario creado con éxito. UID: " + user.uid


def login_with_email_and_password(email, password):
    try:
        user = auth.get_user_by_email(email)
        auth_user = auth.get_user(user)
        return "Inicio de sesión exitoso. UID: " + auth_user.uid
    except firebase_admin.auth.UserNotFoundError:
        return "El usuario no existe."
    except auth.ValueError:
        return "El email o la contraseña son inválidos."
    except auth.FirebaseError as e:
        return "Error al iniciar sesión." + str(e)

# Ejemplo de uso
if __name__ == "__main__":
    email = "example@example.com"
    password = "example_password"
    
    # Intenta iniciar sesión
    print(sign_in_with_email_and_password(email, password))