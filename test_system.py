import pandas as pd
import joblib
import time

# Load the trained AI model
model = joblib.load("threat_detection_model.pkl")

# Test network traffic
test_data = pd.DataFrame(
    [
        [30000, 500],
        [5000, 50],
        [25000, 400],
        [12000, 100]
    ],
    columns=["bytes", "packets"]
)

print("System Functionality Test")
print("-------------------------")

# Measure detection time
start_time = time.time()

predictions = model.predict(test_data)

end_time = time.time()

# Display results
for i, prediction in enumerate(predictions):
    if prediction == 1:
        print(f"Test {i + 1}: 🚨 Threat Detected")
    else:
        print(f"Test {i + 1}: ✅ Normal Activity")

# Calculate performance
detection_time = end_time - start_time

print("\nPerformance Test")
print("----------------")
print("Total detection time:", round(detection_time, 6), "seconds")

print("\nSystem testing completed successfully!")