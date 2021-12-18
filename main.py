from simple_term_menu import TerminalMenu
from tabulate import tabulate
from os import system, name
import datetime
import src.user_class
import src.exercise_digester
import src.food_digester
import src.graph


now = datetime.datetime.now()
in_loop = True


def main():
    food_results = []
    exercise_results = []
    email = input("What is your email? ")
    user = src.user_class.UserClass(email)
    user.check_login()
    clear()
    print(f"Welcome back {user.get_user_string()}!")
    print(f"Last Login: {user.get_last_login()}")

    exercise_digester = src.exercise_digester.ExerciseClass(now, user)
    food_digester = src.food_digester.FoodClass(now, user)

    while in_loop:
        options = ["Display", "Add", "Update", "Delete", "Report", "Quit"]
        terminal_menu = TerminalMenu(options)
        menu_index = terminal_menu.show()
        if options[menu_index] == 'Display':
            clear()
            print('---------------------Daily Report---------------------')
            print('Food')
            print_food(user.select_all_query(food_digester.return_daily_food_query()))
            print('Exercise')
            print_exercise(user.select_all_query(exercise_digester.return_daily_exercise_query()))
        if options[menu_index] == 'Add':
            menu_add_items = ["Food", 'Exercise']
            menu_add = TerminalMenu(menu_add_items)
            menu_add_choice = menu_add.show()
            if menu_add_items[menu_add_choice] == 'Food':
                food_results = food_results + food_digester.get_food_input()
            elif menu_add_items[menu_add_choice] == 'Exercise':
                exercise_results = exercise_results + exercise_digester.get_exercise_input()
        if options[menu_index] == 'Update':
            menu_update_items = ['Food', 'Exercise']
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
            menu_delete_items = ['Food', 'Exercise']
            delete_menu = TerminalMenu(menu_delete_items)
            delete_index = delete_menu.show()
            if menu_delete_items[delete_index] == 'Food':
                user.delete_query(food_digester.delete_food_entry())
                food_results.clear()
            if menu_delete_items[delete_index] == 'Exercise':
                user.delete_query(exercise_digester.delete_exercise_entry())
                exercise_results.clear()
        if options[menu_index] == 'Report':
            menu_report_items = ['Food', 'Exercise']
            report_menu = TerminalMenu(menu_report_items)
            report_index = report_menu.show()
            if menu_report_items[report_index] == 'Food':
                src.graph.report(user.select_all_query(food_digester.weekly_food_report_query()),
                                 report_type='food')
            if menu_report_items[report_index] == 'Exercise':
                src.graph.report(user.select_all_query(exercise_digester.weekly_exercise_report_query()),
                                 report_type='exercise')
        if options[menu_index] == 'Quit':
            user.update_query(user.update_last_login(now))
            exit(0)


def print_food(list_input):
    if type(list_input) is not list:
        return TypeError
    headers = ["Date", "Name", "Quantity", "Calories", "Weight (g)", "User", "UUID"]
    print(tabulate(list_input, headers, tablefmt='simple'))
    print('\n')


def print_exercise(list_input):
    if type(list_input) is not list:
        return TypeError
    headers = ["Date", "Activity", "Calories", "Duration (s)", "User", "UUID"]
    print(tabulate(list_input, headers, tablefmt='simple'))
    print('\n')


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


if __name__ == "__main__":
    main()
