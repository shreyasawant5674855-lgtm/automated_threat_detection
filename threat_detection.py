import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load preprocessed data
data = pd.read_csv("augmented_network_traffic.csv")

# Features and labels
X = data[["bytes", "packets"]]
y = data["label"]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create AI model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train the model
model.fit(X_train, y_train)

print("AI model trained successfully!")
print("Training samples:", len(X_train))