from environs import *
import requests
import datetime
from print_error import print_results


def input_food():
    today = datetime.datetime.today()
    total_cal = 0
    food_id = 0
    return_results = []
    query_results = {}
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
    try:
        req = requests.post(url=endpoint, json=query_json, headers=headers)
    except requests.exceptions.RequestException as exception:
        raise SystemExit(exception)
    print_results("Query", req.status_code)
    req_json = req.json()
    for index, food_list in req_json.items():
        for item in food_list:
            print("----")
            print(f"Name: {item['food_name']}")
            print(f"Quantity: {item['serving_qty']}")
            print(f"Weight (g): {item['serving_weight_grams']}")
            print(f"Calories: {item['nf_calories']}")
            item_cal = int(item['nf_calories'])
            query_results[food_id] = {
                "Food": f"{item['food_name']}",
                "Calories": f"{item['nf_calories']}",
                "Date": f"{today.strftime('%Y/%m/%d')}",
                "Time": f"{today.strftime('%H:%M')}"
            }
            return_results.append(query_results[food_id])
            total_cal = total_cal + item_cal
            food_id += 1
    print("-----------------")
    print(f"Total Calories Consumed: {total_cal}")
    return return_results
