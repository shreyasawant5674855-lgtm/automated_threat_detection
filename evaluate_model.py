import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Load model
model = joblib.load("threat_detection_model.pkl")

# Load test data
data = pd.read_csv("updated_network_traffic.csv")

X = data[["bytes", "packets"]]
y = data["label"]

# Predict
predictions = model.predict(X)

# Calculate performance
accuracy = accuracy_score(y, predictions)
precision = precision_score(y, predictions)
recall = recall_score(y, predictions)

print("Model Evaluation Results")
print("------------------------")
print("Accuracy:", round(accuracy, 2))
print("Precision:", round(precision, 2))
print("Recall:", round(recall, 2))

print("\nModel evaluation completed!")