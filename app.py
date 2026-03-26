from flask import Flask, request, jsonify, render_template
import pickle
import json
import numpy as np

app = Flask(__name__)

# Load model
with open('bangalore_house_price_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load columns
with open('columns.json', 'r') as f:
    data_columns = json.load(f)['data_columns']
    locations = data_columns[3:]


# Home route
@app.route('/')
def index():
    return render_template('index.html')


# Get locations (optional API)
@app.route('/get_locations')
def get_locations():
    return jsonify({'locations': sorted(locations)})


# Prediction logic
def predict_price(location, sqft, bhk, bath):
    x = np.zeros(len(data_columns))

    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if location in data_columns:
        loc_index = data_columns.index(location)
        x[loc_index] = 1

    return model.predict([x])[0]


# Predict API
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    location = data['location']
    sqft = float(data['sqft'])
    bhk = int(data['bhk'])
    bath = int(data['floor'])

    price = predict_price(location, sqft, bhk, bath)

    return jsonify({"price": round(price, 2)})


# Run app (for local testing)
if __name__ == "__main__":
    app.run(debug=True)if __name__ == '__main__':
    app.run(debug=True)