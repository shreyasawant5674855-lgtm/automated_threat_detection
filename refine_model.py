import pandas as pd
import joblib

# Load model
model = joblib.load("threat_detection_model.pkl")

# Test network traffic
test_data = pd.DataFrame(
    [
        [5000, 50],
        [12000, 100],
        [25000, 400],
        [30000, 500]
    ],
    columns=["bytes", "packets"]
)

# Get threat probabilities
probabilities = model.predict_proba(test_data)[:, 1]

# Refined threshold
threshold = 0.70

print("Refined Model Results")
print("---------------------")

for i, probability in enumerate(probabilities):
    if probability >= threshold:
        print(f"Test {i + 1}: 🚨 Threat Detected! Probability: {probability:.2f}")
    else:
        print(f"Test {i + 1}: ✅ Normal Activity. Probability: {probability:.2f}")

print("\nModel refinement completed!")