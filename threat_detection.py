import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
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

# Create Random Forest model
model = RandomForestClassifier(random_state=42)

# Hyperparameters to test
parameters = {
    "n_estimators": [50, 100, 150],
    "max_depth": [3, 5, 10]
}

# Find the best combination
grid_search = GridSearchCV(
    model,
    parameters,
    cv=3,
    scoring="accuracy"
)

grid_search.fit(X_train, y_train)

# Best model
best_model = grid_search.best_estimator_

# Test the best model
y_pred = best_model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Hyperparameter tuning completed!")
print("Best Parameters:", grid_search.best_params_)
print("Accuracy after tuning:", accuracy)