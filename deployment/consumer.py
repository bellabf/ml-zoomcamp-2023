import requests ## to use the POST method we use a library named requests
client = {"job": "unknown", "duration": 270, "poutcome": "failure"}
url = 'http://localhost:9696/predict' ## this is the route we made for prediction
response = requests.post(url, json=client) ## post the customer information in json format
result = response.json() ## get the server response
print(result)