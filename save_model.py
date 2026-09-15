import pandas as pd
import joblib
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

# Save the trained model
joblib.dump(model, "threat_detection_model.pkl")

print("Model trained and saved successfully!")
print("Model file: threat_detection_model.pkl")