import requests
from src.user_class import *
from uuid import uuid1


class ExerciseClass:

    def __init__(self, now, user_class):
        self.user_profile = user_class
        self.time = now
        self.return_results = []
        self.query_results = {}
        self.user = self.user_profile.get_user_id()
        self.endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise/"

    def get_exercise_input(self):
        self.return_results.clear()
        self.query_results.clear()
        self.total_cal = 0
        self.ex_id = 0
        query = input("How did you get off your ass today? ")
        headers = {
            'Content-Type': 'application/json',
            'x-app-id': appid,
            'x-app-key': apikey
        }
        query_json = {
            'query': query,
            'gender': self.user_profile.get_gender(),
            'weight_kg': self.user_profile.get_weight(),
            'height_cm': self.user_profile.get_height(),
            'age': self.user_profile.get_age(),
        }
        try:
            req = requests.post(url=self.endpoint, json=query_json, headers=headers)
        except requests.exceptions.RequestException as exception:
            raise SystemExit(exception)
        req_json = req.json()
        for index, exercise_list in req_json.items():
            for exercise in exercise_list:
                print(f"----")
                print(f"Name: {exercise['user_input']}")
                print(f"Duration (min): {exercise['duration_min']}")
                print(f"Work (cal): {exercise['nf_calories']}")
                item_cal = int(exercise['nf_calories'])
                self.total_cal = self.total_cal + item_cal
                self.query_results[self.ex_id] = {
                    "Exercise": f"{exercise['user_input']}",
                    "Duration": f"{exercise['duration_min']}",
                    "Calories": f"{exercise['nf_calories']}",
                    "Date": f"{self.time.strftime('%Y/%m/%d')}",
                    "Time": f"{self.time.strftime('%H:%M')}"
                }
                self.return_results.append(self.query_results[self.ex_id])
                self.ex_id += 1
        print("-----------------")
        print(f"Total Calories Burned: {self.total_cal}")
        return self.return_results

    def write_query(self, data_point):
        uuid = uuid1()
        user = self.user_profile.get_user_id()
        exercise_insert_query = f"INSERT INTO exercise (date, name, duration, " \
                                f"calories, user, uuid) VALUES " \
                                f"('{self.time.strftime('%Y-%m-%d')}'," \
                                f"'{data_point['Exercise']}'," \
                                f"'{data_point['Duration']}'," \
                                f"'{data_point['Calories']}'," \
                                f"'{user}'," \
                                f"'{uuid}');"
        return exercise_insert_query

    def return_daily_exercise_query(self):
        exercise_daily_select = f"SELECT * from exercise where date = '{self.time.strftime('%Y-%m-%d')}' and user = '{self.user}';"
        return exercise_daily_select

    def delete_exercise_entry(self):
        exercise_daily_delete = f"DELETE from exercise where date = '" \
                            f"{self.time.strftime('%Y-%m-%d')}' and user = '{self.user}';"
        return exercise_daily_delete

    def weekly_exercise_report_query(self):
        weekly_calorie_query = f"SELECT * FROM exercise WHERE date >= DATE(NOW() + interval -7 DAY) and user = '{self.user}';"
        return weekly_calorie_query
