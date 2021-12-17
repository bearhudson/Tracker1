from simple_term_menu import TerminalMenu
import datetime
import src.user_class

now = datetime.datetime.now()


def main():
    email = input("What is your email? ")
    user = src.user_class.UserClass(email)
    user.check_login()
    user_profile = user.get_profile()
    print(f"Welcome back {user_profile[1]}!")
    print(f"Last Login: {user_profile[3]}")
    options = ["Display", "Add", "Update", "Delete"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {menu_entry_index}!")


if __name__ == "__main__":
    main()
