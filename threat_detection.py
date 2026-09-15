import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier

# Load network traffic dataset
data = pd.read_csv("network_traffic.csv")

print("Original Data:")
print(data)

# 1. Handle missing values
data = data.fillna(0)

# 2. Normalize numerical features
features = ["bytes", "packets"]

scaler = MinMaxScaler()
data[features] = scaler.fit_transform(data[features])

print("\nPreprocessed Data:")
print(data)

# Convert labels into numbers
# Normal = 0, Attack = 1
data["label"] = data["label"].map({"Normal": 0, "Attack": 1})

# Features and labels
X = data[["bytes", "packets"]]
y = data["label"]

# Create Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
model.fit(X, y)

# Test sample
sample = [[22000, 350]]

# Normalize test sample
sample = scaler.transform(sample)

# Make prediction
prediction = model.predict(sample)

if prediction[0] == 1:
    print("\nThreat Detected")
else:
    print("\nNormal Activity")

# Save preprocessed data
data.to_csv("preprocessed_network_traffic.csv", index=False)

print("\nData preprocessing completed!")