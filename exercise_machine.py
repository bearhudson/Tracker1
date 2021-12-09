from environs import *
import requests
from print_error import print_results


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
