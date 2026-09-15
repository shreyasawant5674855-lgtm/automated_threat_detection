import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load the trained/preprocessed data
data = pd.read_csv("augmented_network_traffic.csv")

# Features and labels
X = data[["bytes", "packets"]]
y = data["label"]

# Create the AI model
model = RandomForestClassifier(
    n_estimators=50,
    max_depth=3,
    min_samples_split=4,
    min_samples_leaf=2,
    random_state=42
)

# Train the model
model.fit(X, y)

print("AI model integrated with detection system!")

# Sample network traffic
sample = [[22000, 350]]

# Detect threat
prediction = model.predict(sample)

if prediction[0] == 1:
    print("Threat Detected!")
else:
    print("Normal Activity")