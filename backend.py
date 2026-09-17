from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import joblib
import math

app = Flask(__name__)
CORS(app)

# Load the trained AI model once
model = joblib.load("threat_detection_model.pkl")

# Simple cache for previous predictions
prediction_cache = {}


@app.route("/")
def home():
    return jsonify({
        "message": "AI Threat Detection Backend is running!"
    })


@app.route("/detect", methods=["POST"])
def detect_threat():

    data = request.get_json()

    # Check required input
    if not data or "bytes" not in data or "packets" not in data:
        return jsonify({
            "error": "Bytes and packets are required."
        }), 400

    # Validate input
    try:
        bytes_value = float(data["bytes"])
        packets_value = float(data["packets"])
    except (ValueError, TypeError):
        return jsonify({
            "error": "Bytes and packets must be numeric values."
        }), 400

    # Prevent non-finite values such as NaN or infinity
    if not math.isfinite(bytes_value) or not math.isfinite(packets_value):
        return jsonify({
            "error": "Bytes and packets must be finite numeric values."
        }), 400

    # Prevent negative values
    if bytes_value < 0 or packets_value < 0:
        return jsonify({
            "error": "Bytes and packets cannot be negative."
        }), 400

    # Prevent extremely large input values
    if bytes_value > 100000000 or packets_value > 10000000:
        return jsonify({
            "error": "Input values are too large."
        }), 400

    # Create cache key
    cache_key = (bytes_value, packets_value)

    # Check cache
    if cache_key in prediction_cache:
        result = prediction_cache[cache_key]

        return jsonify({
            "result": result,
            "source": "cache"
        })

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

    # Store result in cache
    prediction_cache[cache_key] = result

    return jsonify({
        "result": result,
        "source": "model"
    })


if __name__ == "__main__":
    app.run(debug=True, threaded=True)