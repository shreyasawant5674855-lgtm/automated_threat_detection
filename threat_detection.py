from sklearn.ensemble import RandomForestClassifier

# Sample threat data
X = [
    [10, 2, 1],
    [12, 1, 0],
    [50, 20, 10],
    [45, 18, 8],
    [8, 1, 0],
    [60, 25, 15]
]

# 0 = Normal, 1 = Threat
y = [0, 0, 1, 1, 0, 1]

# Create Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
model.fit(X, y)

# Test sample
sample = [[55, 22, 12]]

# Make prediction
prediction = model.predict(sample)

if prediction[0] == 1:
    print("Threat Detected")
else:
    print("Normal Activity")