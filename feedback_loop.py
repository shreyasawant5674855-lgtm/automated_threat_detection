import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load existing training data
data = pd.read_csv("augmented_network_traffic.csv")

# New threat data received as feedback
new_threat_data = pd.DataFrame({
    "bytes": [25000, 30000],
    "packets": [400, 500],
    "label": [1, 1]
})

# Add new threat data to existing data
data = pd.concat([data, new_threat_data], ignore_index=True)

# Save updated dataset
data.to_csv("updated_network_traffic.csv", index=False)

# Prepare data for training
X = data[["bytes", "packets"]]
y = data["label"]

# Create and retrain the model
model = RandomForestClassifier(
    n_estimators=50,
    max_depth=3,
    min_samples_split=4,
    min_samples_leaf=2,
    random_state=42
)

model.fit(X, y)

print("Feedback loop completed!")
print("New threat data added:", len(new_threat_data))
print("Updated training samples:", len(data))
print("Model updated successfully!")