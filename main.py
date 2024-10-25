from print_functions import *
from account_functions import *


# Welcome Sequence
print("Welcome to the Trust Bank Online Service, I am at your here to assist.")

# User Login.
validation = False
while not validation:
    has_account = input("\n\tDo you already have an account registered with is? [Y/N]: ")

    if has_account.lower() in ["yes", "y"]:
        validation = True
        break
    elif has_account.lower() in ["no", "n"]:
        validation = False
        break
    else:
        print("Invalid option")

if validation == False:
    account = create_account()
else:
    account = login()


# Menu
in_loop = True
while in_loop:
    choice = print_menu(username)
    in_loop = print_choice(choice)
