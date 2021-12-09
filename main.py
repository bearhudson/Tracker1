from food_processor import input_food
from exercise_machine import input_exercise
from sheets_updater import SheetsUpdater
from environs import *

food_input = input_food()
exercise_input = input_exercise()


# workout_sheet = SheetsUpdater(workout_sheet_name)
# print(workout_sheet.get_sheets())
#
# food_sheet = SheetsUpdater(food_sheet_name)
# print(food_sheet.get_sheets())
