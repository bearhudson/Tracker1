import os
import requests


appid = os.environ.get("APPID")
apikey = os.environ.get("APIKEY")
gender = os.environ.get("GENDER")
weight = os.environ.get("WEIGHT")
height = os.environ.get("HEIGHT")
age = os.environ.get("AGE")


def print_results(command, code):
    if code == 200:
        print(f"{command} successful")
    else:
        print(f"{command} failed -> HTTP Response {code}")


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


def input_exercise():
    total_cal = 0
    endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise/"
    query = input("How did you get off your ass today? ")
    headers = {
        'Content-Type': 'application/json',
        'x-app-id': appid,
        'x-app-key': apikey
    }
    query_json = {
        'query': query,
        'gender': gender,
        'weight_kg': weight,
        'height_cm': height,
        'age': age
    }
    try:
        req = requests.post(url=endpoint, json=query_json, headers=headers)
    except requests.exceptions.RequestException as exception:
        raise SystemExit(exception)
    req_json = req.json()
    print_results("Query", req.status_code)
    for exercise_id, exercise_list in req_json.items():
        for exercise in exercise_list:
            print("----")
            print(f"Name: {exercise['user_input']}")
            print(f"Duration (min): {exercise['duration_min']}")
            print(f"Work (cal): {exercise['nf_calories']}")
            item_cal = int(exercise['nf_calories'])
            total_cal = total_cal + item_cal
    print("-----------------")
    print(f"Total Calories: {total_cal}")

input_food()
