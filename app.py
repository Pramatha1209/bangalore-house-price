from flask import Flask, request, jsonify, render_template
import pickle
import json
import numpy as np

app = Flask(__name__)

with open('bangalore_house_price_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('columns.json', 'r') as f:
    data = json.load(f)
    data_columns = data['data_columns']
    locations = data_columns[3:]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_locations')
def get_locations():
    return jsonify({'locations': locations})


def predict_price(location, sqft, bhk, bath):
    x = np.zeros(len(data_columns))

    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    location = location.lower()

    for i in range(len(data_columns)):
        if data_columns[i].lower() == location:
            x[i] = 1
            break

    return model.predict([x])[0]


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    location = data['location']
    sqft = float(data['sqft'])
    bhk = int(data['bhk'])
    bath = int(data['floor'])

    price = predict_price(location, sqft, bhk, bath)

    return jsonify({"price": round(price, 2)})