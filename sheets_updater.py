import requests
from environs import *
from print_error import print_results

headers = {
    "Authorization": f"Bearer {bearertoken}"
}
url = f"https://api.sheety.co/{url_string}"


class SheetsUpdater:

    def __init__(self, sheet_name):
        self.endpoint = f"{url}/{sheet_name}"
        print(self.endpoint)
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

    def add_row(self, **kwargs):
        pass

    def edit_row(self, object_id, **kwargs):
        pass

    def delete_row(self, object_id, **kwargs):
        pass