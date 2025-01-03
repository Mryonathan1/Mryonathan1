from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/') 
def home():
    return "Flask app is running!"


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # Example response
    return jsonify({'message': 'Prediction received', 'data': data})

if __name__ == '__main__':
    app.run(debug=True)
