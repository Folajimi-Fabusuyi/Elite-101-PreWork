import os

from account_functions import *
from chatbot_functions import *
from account_storing import *

# Welcome Sequence
print("Welcome to the Trust-Bank Online Service, I am your assistant ChatBot")

# User Login.
validation = False
while not validation:
    has_account = input("\tDo you already have an account registered with is? [Y/N]: ")

    if has_account.lower() in ["yes", "y"]:
        validation = True
        break
    elif has_account.lower() in ["no", "n"]:
        validation = False
        break
    else: print("Invalid option")

if not validation: account = create_account()
else: account = login()

# TODO: Semi-Urgent: Add comments and documentation
# TODO: URGENT: Work on bot commands
# TODO: URGENT: Have different bot commands for each account. Possible make the bot a class

# Menu
in_loop = True
while in_loop:
    os.system('cls' if os.name == 'nt' else 'clear')
    save_account(account)

    print(account[0])
    print(account[1])

    while True:
        if account == None:
            in_loop = False
            break
        account = chat_bot(account)