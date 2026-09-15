from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import joblib

app = Flask(__name__)
CORS(app)

# Load the trained AI model
model = joblib.load("threat_detection_model.pkl")


@app.route("/")
def home():
    return jsonify({
        "message": "AI Threat Detection Backend is running!"
    })


@app.route("/detect", methods=["POST"])
def detect_threat():

    data = request.get_json()

    # Check if required data is present
    if not data or "bytes" not in data or "packets" not in data:
        return jsonify({
            "error": "Bytes and packets are required."
        }), 400

    # Validate numeric input
    try:
        bytes_value = float(data["bytes"])
        packets_value = float(data["packets"])
    except (ValueError, TypeError):
        return jsonify({
            "error": "Bytes and packets must be numeric values."
        }), 400

    # Prevent negative values
    if bytes_value < 0 or packets_value < 0:
        return jsonify({
            "error": "Bytes and packets cannot be negative."
        }), 400

    # Prepare data for AI model
    network_data = pd.DataFrame(
        [[bytes_value, packets_value]],
        columns=["bytes", "packets"]
    )

    # Predict threat
    prediction = model.predict(network_data)

    if prediction[0] == 1:
        result = "Threat Detected"
    else:
        result = "Normal Activity"

    return jsonify({
        "result": result
    })


if __name__ == "__main__":
    app.run(debug=True)