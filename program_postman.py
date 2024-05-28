import requests
import json

# Define the API endpoint URL
url = "https://automationexercise.com/api/productsList"

# Define the headers with the API key
headers = {'X-API-Key': '{{token}}'}

# Make the GET request
response = requests.request("GET", url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Convert the response to JSON format
    json_response = response.json()

    # Save the JSON response to a file with better formatting
    with open('response.json', 'w') as file:
        json.dump(json_response, file, indent=4)

    print("The response has been saved to response.json")
else:
    print("Error during the request:", response.status_code)

