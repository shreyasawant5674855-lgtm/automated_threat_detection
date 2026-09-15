import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load preprocessed data
data = pd.read_csv("augmented_network_traffic.csv")

# Features and labels
X = data[["bytes", "packets"]]
y = data["label"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Random Forest with regularization to prevent overfitting
model = RandomForestClassifier(
    n_estimators=50,
    max_depth=3,
    min_samples_split=4,
    min_samples_leaf=2,
    random_state=42
)

# Train the model
model.fit(X_train, y_train)

# Test the model
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Overfitting prevention completed!")
print("Max Depth:", model.max_depth)
print("Minimum Samples Split:", model.min_samples_split)
print("Minimum Samples Leaf:", model.min_samples_leaf)
print("Model Accuracy:", accuracy)