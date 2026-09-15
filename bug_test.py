import pandas as pd
import joblib

print("Bug Testing Started")
print("-------------------")

# Load the trained model
model = joblib.load("threat_detection_model.pkl")

# Test different inputs
test_cases = [
    [30000, 500],
    [5000, 50],
    [25000, 400]
]

for i, test_case in enumerate(test_cases):
    try:
        data = pd.DataFrame(
            [test_case],
            columns=["bytes", "packets"]
        )

        prediction = model.predict(data)

        if prediction[0] == 1:
            print(f"Test {i + 1}: Threat Detected - No Error")
        else:
            print(f"Test {i + 1}: Normal Activity - No Error")

    except Exception as error:
        print(f"Test {i + 1}: Bug Found - {error}")

print("-------------------")
print("Bug testing completed!")