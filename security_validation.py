import requests

url = "http://127.0.0.1:5000/detect"

print("Security Validation Started")
print("---------------------------")

test_cases = [
    {
        "name": "Valid Input",
        "data": {
            "bytes": 30000,
            "packets": 500
        }
    },
    {
        "name": "Invalid Text",
        "data": {
            "bytes": "abc",
            "packets": "xyz"
        }
    },
    {
        "name": "Negative Values",
        "data": {
            "bytes": -100,
            "packets": -10
        }
    },
    {
        "name": "Very Large Values",
        "data": {
            "bytes": 999999999,
            "packets": 999999
        }
    }
]

for test in test_cases:

    response = requests.post(
        url,
        json=test["data"]
    )

    print("\nTest:", test["name"])
    print("Status Code:", response.status_code)
    print("Response:", response.text)

print("\nSecurity validation completed!")