import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load the augmented/preprocessed data
data = pd.read_csv("augmented_network_traffic.csv")

# Features and target
X = data[["bytes", "packets"]]
y = data["label"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create the AI model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train the AI model
model.fit(X_train, y_train)

# Check model accuracy
accuracy = model.score(X_test, y_test)

print("AI model training completed!")
print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))
print("Model Accuracy:", accuracy)

# Test a new network activity
sample = [[22000, 350]]

prediction = model.predict(sample)

if prediction[0] == 1:
    print("Threat Detected")
else:
    print("Normal Activity")