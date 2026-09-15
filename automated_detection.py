import pandas as pd
import joblib

# Load the trained model
model = joblib.load("threat_detection_model.pkl")

print("Automated threat detection system started!")

# Incoming network traffic
network_data = pd.DataFrame(
    [
        [30000, 500],
        [5000, 50]
    ],
    columns=["bytes", "packets"]
)

# Detect threats automatically
predictions = model.predict(network_data)

for i, prediction in enumerate(predictions):
    if prediction == 1:
        print(f"Traffic {i + 1}: 🚨 Threat Detected!")
    else:
        print(f"Traffic {i + 1}: ✅ Normal Activity")

print("Automated threat detection completed!")