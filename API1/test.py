import requests
BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'apijsoncbv1/'
resp = requests.delete(BASE_URL + ENDPOINT)
data = resp.json()
print(data)




