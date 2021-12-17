import requests
from src.environs import *


class FoodClass:
    def __init__(self, now):
        self.time = now
        self.return_results = []
        self.query_results = {}
        self.endpoint = "https://trackapi.nutritionix.com/v2/natural/nutrients/"
        self.req_json = {}

    def get_food_input(self):
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
            req = requests.post(url=self.endpoint, json=query_json, headers=headers)
        except requests.exceptions.RequestException as exception:
            raise SystemExit(exception)
        self.req_json = req.json()
        food_id = 0
        total_cal = 0

        for index, food_list in self.req_json.items():
            for item in food_list:
                print("----")
                print(f"Name: {item['food_name']}")
                print(f"Quantity: {item['serving_qty']}")
                print(f"Weight (g): {item['serving_weight_grams']}")
                print(f"Calories: {item['nf_calories']}")
                item_cal = int(item['nf_calories'])
                self.query_results[food_id] = {
                    "Food": f"{item['food_name']}",
                    "Calories": f"{item['nf_calories']}",
                    "Date": f"{self.time.strftime('%Y/%m/%d')}",
                    "Time": f"{self.time.strftime('%H:%M')}"
                }
                self.return_results.append(self.query_results[food_id])
                total_cal = total_cal + item_cal
                food_id += 1
        return self.return_results
