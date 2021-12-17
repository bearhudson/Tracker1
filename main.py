import os

from simple_term_menu import TerminalMenu
import datetime
import src.user_class
import src.exercise_digester
import src.food_digester
from tabulate import tabulate
from os import system

now = datetime.datetime.now()
in_loop = True


def main():
    food_results = []
    exercise_results = []
    email = input("What is your email? ")
    user = src.user_class.UserClass(email)
    user.check_login()
    print(f"Welcome back {user.get_user_string()}!")
    print(f"Last Login: {user.get_last_login()}")

    exercise_digester = src.exercise_digester.ExerciseClass(now, user)
    food_digester = src.food_digester.FoodClass(now, user)

    while in_loop:
        options = ["Display", "Add", "Update", "Delete"]
        terminal_menu = TerminalMenu(options)
        menu_index = terminal_menu.show()

        if options[menu_index] == 'Display':
            print("\n---------------------Daily Report---------------------")
            print("Food")
            print_food(user.select_all_query(food_digester.return_daily_food_query()))
            print("Exercise")
            print_exercise(user.select_all_query(exercise_digester.return_daily_exercise_query()))
        if options[menu_index] == 'Add':
            menu_add_items = ["Food", "Exercise"]
            menu_add = TerminalMenu(menu_add_items)
            menu_add_choice = menu_add.show()
            if menu_add_items[menu_add_choice] == 'Food':
                food_results = food_results + food_digester.get_food_input()
            elif menu_add_items[menu_add_choice] == 'Exercise':
                exercise_results = exercise_results + exercise_digester.get_exercise_input()
        if options[menu_index] == 'Update':
            menu_update_items = ["Food", "Exercise"]
            menu_update = TerminalMenu(menu_update_items)
            menu_update_choice = menu_update.show()
            if menu_update_items[menu_update_choice] == 'Food':
                for food_item in food_results:
                    user.user_insert_query(food_digester.write_query(food_item))
                    food_results = []
            elif menu_update_items[menu_update_choice] == 'Exercise':
                for exercise_item in exercise_results:
                    user.user_insert_query(exercise_digester.write_query(exercise_item))
                    exercise_results = []
        if options[menu_index] == 'Delete':
            menu_delete_items = []
            if len(food_results) > 0:
                menu_delete_items = menu_delete_items + ['Food']
            if len(exercise_results) > 0:
                menu_delete_items = menu_delete_items + ['Exercise']
            delete_menu = TerminalMenu(menu_delete_items)
            delete_index = delete_menu.show()
            if menu_delete_items[delete_index] == 'Food':
                food_results.clear()
            if menu_delete_items[delete_index] == 'Exercise':
                exercise_results.clear()
    os.system('clear')


def print_food(list_input):
    if type(list_input) is not list:
        return TypeError
    headers = ["Date", "Name", "Quantity", "Calories", "Weight (g)", "User", "UUID"]
    print(tabulate(list_input, headers, tablefmt='simple'))


def print_exercise(list_input):
    if type(list_input) is not list:
        return TypeError
    headers = ["Date", "Activity", "Calories", "Duration (s)", "User", "UUID"]
    print(tabulate(list_input, headers, tablefmt='simple'))


if __name__ == "__main__":
    main()
