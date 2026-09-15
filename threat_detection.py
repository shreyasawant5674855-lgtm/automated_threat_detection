import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load the dataset
data = pd.read_csv("network_traffic.csv")

# Handle missing values
data = data.fillna(0)

# Normalize numerical features
features = ["bytes", "packets"]

scaler = MinMaxScaler()
data[features] = scaler.fit_transform(data[features])

# Convert labels into numbers
# Normal = 0, Attack = 1
data["label"] = data["label"].map({"Normal": 0, "Attack": 1})

# -------------------------------
# 4. DATA AUGMENTATION
# -------------------------------

# Create copies of the original data
augmented_data = data.copy()

# Add small random variations
np.random.seed(42)

augmented_data["bytes"] += np.random.normal(0, 0.02, len(data))
augmented_data["packets"] += np.random.normal(0, 0.02, len(data))

# Combine original and augmented data
data = pd.concat([data, augmented_data], ignore_index=True)

print("Original dataset size:", len(data) // 2)
print("Augmented dataset size:", len(data))

# Save augmented dataset
data.to_csv("augmented_network_traffic.csv", index=False)

# -------------------------------
# TRAINING AND TESTING
# -------------------------------

X = data[["bytes", "packets"]]
y = data["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))

# Create Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Test the model
prediction = model.predict(X_test)

print("Predictions:", prediction)
print("Data augmentation completed!")