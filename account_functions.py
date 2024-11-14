import os
import getpass

from password_functions import decrypt_password
from account_storing import load_file
from accounts import CheckingsAccount, CreditAccount


def create_account():
    print("\tYou will now begin the account creation process")

    database = load_file()
    email = input("\t\033[1m• Email:\033[0m ")

    while email in [account[0]["email"] for account in database]:
        print("\t\033[91m\033[1mEmail already exists.\033[0m")
        email = input("\t\033[1m• Email:\033[0m")

    password = getpass.getpass("\t\033[1m• Password \033[91m[WILL NOT SHOW FOR SECURITY]\033[0m\033[1m:\033[0m ")
    user_info = [input("\t\033[1m• Name:\033[0m "), input("\t\033[1m• Address:\033[0m "),
                 input("\t\033[1m• Age:\033[0m ")]

    os.system('cls' if os.name == 'nt' else 'clear')

    return [CheckingsAccount(email=email, password=password, user_info=user_info),
            CreditAccount(email=email, password=password, user_info=user_info)]


# TODO: Optional: Add a login attempt limit
def login():
    print("\tYou will now begin the login process")
    database = load_file()
    attempted_account = None

    email = input("\t\033[1m• Email: \033[0m")
    while email not in [account[0]["email"] for account in database]:
        print("\t\033[91m\033[1mEmail doesn't exists.\033[0m")
        email = input("\t\033[1m• Email: \033[0m")

    for account in database:
        if account[0]["email"] == email:
            attempted_account = account

    password = getpass.getpass("\t\033[1m• Password \033[91m[WILL NOT SHOW FOR SECURITY]\033[0m\033[1m:\033[0m ")
    while password != decrypt_password(attempted_account[0]["password"]):
        print("\t\033[91m\033[1mIncorrect password. Try Again\033[0m")
        password = getpass.getpass("\t\033[1m• Password:\033[0m ")

    print("\t\033[92m\033[1mLogin Successful\033[0m")

    acc = attempted_account
    checkings_account = CheckingsAccount(acc[0]["email"], decrypt_password(acc[0]["password"]), acc[0]["level"],
                                         acc[0]["user_info"], acc[0]["balance"])
    credit_account = CreditAccount(acc[1]["email"], decrypt_password(acc[1]["password"]), acc[1]["level"],
                                   acc[1]["user_info"], acc[1]["date_opened"], acc[1]["credit_score"], acc[1]["loan_balance"],
                                   acc[1]["transactions"])
    return [checkings_account, credit_account]


if __name__ == "__main__":
    # new_account = CheckingsAccount(level=3, password="testing123$@()4", user_info=["Daniel Fabusuyi", "1532 Transit Parkway", 35], email="folajimifabusuyi@gmail.com")
    # new_account = create_account()
    # print(decrypt_password(new_account.password))

    new_account = CreditAccount(level=0)
    print(new_account.credit_score, new_account.loan_limit)
    new_account.credit_score_update()
    new_account.update_account()
    print(new_account.credit_score, new_account.loan_limit)
    print(new_account)