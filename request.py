import requests
data = {
    "sepal_length": 2,
    "sepal_width":5,
    "petal_length":4,
    "petal_width":2
  }

url = "http://127.0.0.1:5000/predict_api"
response = requests.post(url, json=data)
print("Churn: " + str(response.json()))