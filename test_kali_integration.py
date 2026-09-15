import pandas as pd
import joblib

# Load the trained model
model = joblib.load("threat_detection_model.pkl")

print("Testing model integration...")

test_data = pd.DataFrame(
    [
        [30000, 500],
        [5000, 50],
        [25000, 400]
    ],
    columns=["bytes", "packets"]
)

predictions = model.predict(test_data)

for i, prediction in enumerate(predictions):
    if prediction == 1:
        print(f"Test {i + 1}: 🚨 Threat Detected!")
    else:
        print(f"Test {i + 1}: ✅ Normal Activity")

print("Integration testing completed!")