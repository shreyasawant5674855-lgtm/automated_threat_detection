import requests

print("Security Testing Started")
print("------------------------")

url = "http://127.0.0.1:5000/detect"

# Test valid input
valid_data = {
    "bytes": 30000,
    "packets": 500
}

try:
    response = requests.post(url, json=valid_data)

    print("Valid Input Test:")
    print("Status Code:", response.status_code)
    print("Response:", response.json())

except Exception as error:
    print("Valid Input Test Error:", error)


# Test invalid input
invalid_data = {
    "bytes": "abc",
    "packets": "xyz"
}

try:
    response = requests.post(url, json=invalid_data)

    print("\nInvalid Input Test:")
    print("Status Code:", response.status_code)
    print("Response:", response.text)

except Exception as error:
    print("Invalid Input Test Error:", error)

print("\nSecurity testing completed!")