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

# New network traffic to check
sample = pd.DataFrame(
    [[30000, 500]],
    columns=["bytes", "packets"]
)

# Predict threat
prediction = model.predict(sample)

# Generate alert
if prediction[0] == 1:
    print("🚨 ALERT: Threat Detected!")
    print("Notification: Suspicious network activity detected.")
else:
    print("✅ No Threat Detected.")
    print("Notification: Network activity is normal.")