import requests
from src.environs import *
from uuid import uuid1


class FoodClass:
    def __init__(self, now, user_class):
        self.user_profile = user_class
        self.time = now
        self.return_results = []
        self.query_results = {}
        self.endpoint = "https://trackapi.nutritionix.com/v2/natural/nutrients/"
        self.req_json = {}

    def get_food_input(self):
        self.return_results.clear()
        self.query_results.clear()
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

    def write_query(self, data_point):
        uuid = uuid1()
        user = self.user_profile.get_user_id()
        food_insert_query = f"INSERT INTO food (date, name, calories, user, uuid) VALUES " \
                            f"('{self.time.strftime('%Y-%m-%d')}'," \
                            f"'{data_point['Food']}'," \
                            f"'{data_point['Calories']}'," \
                            f"'{user}'," \
                            f"'{uuid}');"
        return food_insert_query
