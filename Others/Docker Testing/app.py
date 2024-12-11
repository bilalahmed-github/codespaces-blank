from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

import requests

API_URL = "http://API_CALLING_SERVICE_IP:8000"  # Change API_CALLING_SERVICE_IP to the actual IP

@app.route('/get_users_from_api', methods=['GET'])
def get_users_from_api():
    response = requests.get(f"{API_URL}/users")
    if response.status_code == 200:
        users = response.json()  # Assuming JSON response
        return {"message": "Successfully retrieved users", "users": users}
    return {"message": "Failed to retrieve users"}
