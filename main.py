from simple_term_menu import TerminalMenu
import datetime
import src.user_class
import src.run_digester
import src.food_digester

now = datetime.datetime.now()

in_loop = True


def main():
    results = []
    email = input("What is your email? ")
    user = src.user_class.UserClass(email)
    user.check_login()
    user_profile = user.get_profile()
    print(f"Welcome back {user_profile[1]}!")
    print(f"Last Login: {user_profile[3]}")

    while in_loop:
        food_digester = src.food_digester.FoodClass(now)
        options = ["Display", "Add", "Update", "Delete"]
        terminal_menu = TerminalMenu(options)
        menu_index = terminal_menu.show()

        if options[menu_index] == 'Display':
            print(results)
        if options[menu_index] == 'Add':
            results.append(food_digester.get_food_input())
            print(results)
        if options[menu_index] == 'Update':
            print("Update!")
        if options[menu_index] == 'Delete':
            for i in range(len(results)):
                print(results[i])


if __name__ == "__main__":
    main()
