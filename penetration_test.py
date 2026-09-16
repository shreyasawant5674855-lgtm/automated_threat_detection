import requests

url = "http://127.0.0.1:5000/detect"

print("Penetration Testing Started")
print("---------------------------")

test_cases = [
    {
        "name": "Empty Request",
        "data": {}
    },
    {
        "name": "Text Input",
        "data": {
            "bytes": "test",
            "packets": "test"
        }
    },
    {
        "name": "Negative Input",
        "data": {
            "bytes": -5000,
            "packets": -100
        }
    },
    {
        "name": "Very Large Input",
        "data": {
            "bytes": 999999999,
            "packets": 999999
        }
    }
]

for test in test_cases:

    try:
        response = requests.post(
            url,
            json=test["data"]
        )

        print("\nTest:", test["name"])
        print("Status Code:", response.status_code)
        print("Response:", response.text)

    except Exception as error:
        print("\nTest:", test["name"])
        print("Error:", error)

print("\nPenetration testing completed!")