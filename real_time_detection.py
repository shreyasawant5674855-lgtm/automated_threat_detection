import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import time

# Load updated training data
data = pd.read_csv("updated_network_traffic.csv")

# Features and labels
X = data[["bytes", "packets"]]
y = data["label"]

# Optimized Random Forest model
model = RandomForestClassifier(
    n_estimators=50,
    max_depth=3,
    min_samples_split=4,
    min_samples_leaf=2,
    random_state=42,
    n_jobs=-1
)

# Train the model
model.fit(X, y)

print("Real-time threat detection model ready!")

# Simulated incoming network traffic
sample = pd.DataFrame(
    [[30000, 500]],
    columns=["bytes", "packets"]
)

# Measure detection time
start_time = time.time()

prediction = model.predict(sample)

end_time = time.time()

detection_time = end_time - start_time

if prediction[0] == 1:
    print("🚨 Threat Detected!")
else:
    print("✅ Normal Activity")

print("Detection time:", round(detection_time, 6), "seconds")
print("Real-time optimization completed!")