import datetime

from src.environs import *
import requests
from print_error import print_results


def input_exercise():
    today = datetime.datetime.today()
    total_cal = 0
    ex_id = 0
    return_results = []
    query_results = {}
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
        'age': age,
    }
    try:
        req = requests.post(url=endpoint, json=query_json, headers=headers)
    except requests.exceptions.RequestException as exception:
        raise SystemExit(exception)
    req_json = req.json()
    print_results("Query", req.status_code)
    for index, exercise_list in req_json.items():
        for exercise in exercise_list:
            print(f"----")
            print(f"Name: {exercise['user_input']}")
            print(f"Duration (min): {exercise['duration_min']}")
            print(f"Work (cal): {exercise['nf_calories']}")
            item_cal = int(exercise['nf_calories'])
            total_cal = total_cal + item_cal
            query_results[ex_id] = {
                "Exercise": f"{exercise['user_input']}",
                "Duration": f"{exercise['duration_min']}",
                "Calories": f"{exercise['nf_calories']}",
                "Date": f"{today.strftime('%Y/%m/%d')}",
                "Time": f"{today.strftime('%H:%M')}"
            }
            return_results.append(query_results[ex_id])
            ex_id += 1
    print("-----------------")
    print(f"Total Calories Burned: {total_cal}")
    return return_results
