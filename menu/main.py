import functions_framework
from menu import get_restaurant_menu

# Error handler for AssertionError
@functions_framework.errorhandler(AssertionError)
def handle_assertion_error(e):
    body = {"msg": "Method not allowed"}
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET",
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Max-Age": "3600"
    }
    return body, 405, headers

# Main function to handle GET and OPTIONS requests
@functions_framework.http
def get_menu(request):
    # Set CORS headers for the preflight request
    if request.method == "OPTIONS":
        headers = {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Max-Age": "3600"
        }
        return ("", 204, headers)

    # Set CORS headers for the main request
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET",
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Max-Age": "3600"
    }

    # Ensure only GET requests are allowed
    if request.method != "GET":
        raise AssertionError

    menu_json = get_restaurant_menu()
    return menu_json, 200, headers
