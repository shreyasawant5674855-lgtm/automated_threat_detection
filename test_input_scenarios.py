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

# Different network traffic scenarios
scenarios = pd.DataFrame(
    [
        [5000, 50],       # Low traffic
        [12000, 100],     # Medium traffic
        [30000, 500],     # High traffic
        [25000, 400]      # Suspicious traffic
    ],
    columns=["bytes", "packets"]
)

# Test each scenario
predictions = model.predict(scenarios)

print("Testing various input scenarios:\n")

for i, prediction in enumerate(predictions):
    if prediction == 1:
        print(f"Scenario {i + 1}: 🚨 Threat Detected")
    else:
        print(f"Scenario {i + 1}: ✅ Normal Activity")

print("\nVarious input scenario testing completed!")