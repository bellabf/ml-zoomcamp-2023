import requests ## to use the POST method we use a library named requests
url = "http://0.0.0.0:9696/predict"
client = {"job": "retired", "duration": 445, "poutcome": "success"}
response = requests.post(url, json=client) ## post the customer information in json format
result = response.json() ## get the server response
print(result)