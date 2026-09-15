import pandas as pd
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

# Features and labels
X = data[["bytes", "packets"]]
y = data["label"]

# 3. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training data:")
print(X_train)

print("\nTesting data:")
print(X_test)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))

# Create Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Test the model
prediction = model.predict(X_test)

print("\nModel testing completed!")
print("Predictions:", prediction)