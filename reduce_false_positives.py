import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load training data
data = pd.read_csv("updated_network_traffic.csv")

# Features and labels
X = data[["bytes", "packets"]]
y = data["label"]

# Train the model
model = RandomForestClassifier(
    n_estimators=50,
    max_depth=3,
    min_samples_split=4,
    min_samples_leaf=2,
    random_state=42
)

model.fit(X, y)

# Sample network traffic
samples = pd.DataFrame(
    [
        [5000, 50],
        [12000, 100],
        [30000, 500]
    ],
    columns=["bytes", "packets"]
)

# Get threat probabilities
probabilities = model.predict_proba(samples)[:, 1]

# Set a higher threshold to reduce false positives
threshold = 0.70

print("False positive reduction test:")

for i, probability in enumerate(probabilities):
    if probability >= threshold:
        print(f"Test {i + 1}: 🚨 Threat Detected! Probability: {probability:.2f}")
    else:
        print(f"Test {i + 1}: ✅ Normal Activity. Probability: {probability:.2f}")

print("False positive reduction completed!")