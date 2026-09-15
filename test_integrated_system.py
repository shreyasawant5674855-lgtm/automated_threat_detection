import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load updated data
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

# Sample test data
test_data = pd.DataFrame({
    "bytes": [30000, 5000],
    "packets": [500, 50]
})

# Predict
predictions = model.predict(test_data)

print("Integrated system testing started!")

for i, prediction in enumerate(predictions):
    if prediction == 1:
        print(f"Test {i + 1}: 🚨 Threat Detected!")
    else:
        print(f"Test {i + 1}: ✅ Normal Activity")

print("Integrated system testing completed!")