from flask import Flask, request

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.json
    # Process the data
    return "Data received and processed"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
