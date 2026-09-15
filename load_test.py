import requests
import time

url = "http://127.0.0.1:5000/detect"

test_data = {
    "bytes": 30000,
    "packets": 500
}

number_of_requests = 50

print("Heavy Load Testing Started")
print("--------------------------")
print("Number of requests:", number_of_requests)

start_time = time.time()

successful_requests = 0

for i in range(number_of_requests):

    response = requests.post(url, json=test_data)

    if response.status_code == 200:
        successful_requests += 1

end_time = time.time()

total_time = end_time - start_time

print("\nLoad Test Results")
print("-----------------")
print("Successful requests:", successful_requests)
print("Total time:", round(total_time, 4), "seconds")
print("Average response time:",
      round(total_time / number_of_requests, 6), "seconds")

print("\nHeavy load testing completed!")