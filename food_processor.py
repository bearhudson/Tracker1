from environs import *
import requests
from print_error import print_results


def input_food():
    endpoint = "https://trackapi.nutritionix.com/v2/natural/nutrients/"
    query = input("What do you shove down your gullet today? ")
    headers = {
        'Content-Type': 'application/json',
        'x-app-id': appid,
        'x-app-key': apikey
    }
    query_json = {
        'query': query,
    }
    total_cal = 0
    try:
        req = requests.post(url=endpoint, json=query_json, headers=headers)
    except requests.exceptions.RequestException as exception:
        raise SystemExit(exception)
    print_results("Query", req.status_code)
    req_json = req.json()
    for food_id, food_list in req_json.items():
        for item in food_list:
            print(f"Name: {item['food_name']}")
            print(f"Quantity: {item['serving_qty']}")
            print(f"Weight: {item['serving_weight_grams']}")
            print(f"Calories: {item['nf_calories']}")
            item_cal = int(item['nf_calories'])
            total_cal = total_cal + item_cal
    print("-----------------")
    print(f"Total Calories: {total_cal}")
