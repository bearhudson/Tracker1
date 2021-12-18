import requests
from src.environs import *
from uuid import uuid1


class FoodClass:
    def __init__(self, now, user_object):
        self.user_profile = user_object
        self.time = now
        self.return_results = []
        self.query_results = {}
        self.req_json = {}
        self.user = self.user_profile.get_user_id()
        self.endpoint = "https://trackapi.nutritionix.com/v2/natural/nutrients/"

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
                    "Quantity": f"{item['serving_qty']}",
                    "Weight": f"{item['serving_weight_grams']}",
                    "Date": f"{self.time.strftime('%Y/%m/%d')}",
                    "Time": f"{self.time.strftime('%H:%M')}"
                }
                self.return_results.append(self.query_results[food_id])
                total_cal = total_cal + item_cal
                food_id += 1
        return self.return_results

    def write_query(self, data_point):
        uuid = uuid1()
        food_insert_query = f"INSERT INTO food (date, name, quantity, calories, weight, user, uuid) VALUES " \
                            f"('{self.time.strftime('%Y-%m-%d')}'," \
                            f"'{data_point['Food']}'," \
                            f"'{data_point['Quantity']}'," \
                            f"'{data_point['Calories']}'," \
                            f"'{data_point['Weight']}'," \
                            f"'{self.user}'," \
                            f"'{uuid}');"
        return food_insert_query

    def return_daily_food_query(self):
        food_daily_select = f"SELECT * from food where date = '" \
                            f"{self.time.strftime('%Y-%m-%d')}' and user = '{self.user}';"
        return food_daily_select

    def delete_food_entry(self):
        food_daily_delete = f"DELETE from food where date = '" \
                            f"{self.time.strftime('%Y-%m-%d')}' and user = '{self.user}';"
        return food_daily_delete

    def weekly_food_report_query(self):
        weekly_calorie_query = f"SELECT * FROM food WHERE date >= DATE(NOW() + interval -7 DAY) and user = {self.user};"
        return weekly_calorie_query
