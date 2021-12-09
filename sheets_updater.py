import requests
from environs import *
from print_error import print_results

headers = {
    "Authorization": f"Bearer {bearertoken}",
    "Content-Type": "application/json",
}
url = f"https://api.sheety.co/{url_string}"


class SheetsUpdater:

    def __init__(self, sheet_name):
        self.endpoint = f"{url}/{sheet_name}"
        self.get_req = None
        self.get_req_json = {}
        self.add_req = None
        self.add_req_json = {}
        self.edit_req = None
        self.edit_req_json = {}
        self.delete_req = None
        self.delete_req_json = {}

    def get_sheets(self):
        try:
            self.get_req = requests.get(url=self.endpoint, headers=headers)
        except requests.exceptions.RequestException as exception:
            raise SystemExit(exception)
        print_results("Get", self.get_req.status_code)
        self.get_req_json = self.get_req.json()
        return self.get_req_json

    def add_row(self, entry_type, add_object):
        if entry_type == "workout":
            payload = {
                "workout": {
                    "Date": add_object["Date"],
                    "Time": add_object["Time"],
                    "Exercise": add_object["Exercise"],
                    "Duration": add_object["Duration"],
                    "Calories": add_object["Calories"]
                }
            }
        elif entry_type == "food":
            payload = {
                "food": {
                    "Date": add_object["Date"],
                    "Food": add_object["Food"],
                    "Calories": add_object["Calories"]
                }
            }
        else:
            print("Error")

        print(self.endpoint)
        try:
            self.add_req = requests.post(url=self.endpoint, json=payload, headers=headers)
        except requests.exceptions.RequestException as exception:
            raise SystemExit(exception)
        print_results("Post", self.add_req.status_code)
        print(self.add_req.text)

    def edit_row(self, object_id, *args):
        pass

    def delete_row(self, object_id, *args):
        pass
