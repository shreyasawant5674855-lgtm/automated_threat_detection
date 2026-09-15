from flask import Flask, jsonify, request
import pandas as pd
import joblib

app = Flask(__name__)

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

    bytes_value = data["bytes"]
    packets_value = data["packets"]

    network_data = pd.DataFrame(
        [[bytes_value, packets_value]],
        columns=["bytes", "packets"]
    )

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