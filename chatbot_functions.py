from account_storing import save_account
import os


def chat_bot(account):
    option = input("-"*86 + "\n|  Deposit[D]  |  Pay Balance[P]  |  Withdraw[W]  |  View[V]  |  Save[S]  | Quit[Q]  |\n" + "-"*86 + "\n\t\t\t\tOption: ")
    if option.lower() == "q":
        account = None
    else:
        account = chat_bot_options(account, option)

    return account


def chat_bot_options(account, option):
    if option.upper() == "S":
        save_account(account)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\t\033[93mAccount Saved\033[0m")
    else:
        print("Not implemented yet please try later.")

    return account
