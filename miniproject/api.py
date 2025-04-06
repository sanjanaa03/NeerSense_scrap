from flask import Flask, request, jsonify, send_file
import pandas as pd
import joblib
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enables Cross-Origin requests (for Flutter web support)

# Load the trained model
model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    return jsonify({'predicted_water_consumption': prediction})

@app.route('/plot', methods=['GET'])
def get_plot():
    try:
        return send_file('prediction_plot.png', mimetype='image/png')
    except FileNotFoundError:
        return jsonify({'error': 'Plot image not found. Please generate it first.'}), 404

@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'API is running!'})

if __name__ == '__main__':
    app.run(debug=True, host='192.168.xx.x') #your ip address
