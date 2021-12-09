import os
import requests


endpoint = "https://trackapi.nutritionix.com/v2/natural/nutrients/"
appid = os.environ.get("APPID")
apikey = os.environ.get("APIKEY")


def print_results(command, code):
    if code == 200:
        print(f"{command} successful")
    else:
        print(f"{command} failed -> HTTP Response {code}")


query = input("What do you shove down your gullet today? ")

headers = {
    'Content-Type': 'application/json',
    'x-app-id': appid,
    'x-app-key': apikey
}

query_json = {
    'query': query
}

try:
    req = requests.post(url=endpoint, json=query_json, headers=headers)
except requests.exceptions.RequestException as exception:
    raise SystemExit(exception)
print_results("Query", req.status_code)
req_json = req.json()
print(type(req_json))
