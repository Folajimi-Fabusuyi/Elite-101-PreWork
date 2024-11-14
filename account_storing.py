import os
import json

from accounts import CheckingsAccount, CreditAccount


def load_file():
    # Checks if file exists and isn't empty then loads the file content
    if os.path.isfile("accounts.json"):
        if os.stat("accounts.json").st_size != 0:
            with open("accounts.json", "r") as file:
                data = json.load(file)
                return data
    return []


def save_account(account):
    data = load_file()

    # Checks for if account we are saving already exists
    for i in data:
        if account[0].email == i[0]["email"]:
            index = data.index(i)
            data[index] = ([
                {
                    "email": account[0].email,
                    "password": account[0].password,
                    "type": account[0].type,
                    "details": account[0].details,
                    "balance": account[0].balance,
                    "user_info": account[0].user_info,
                    "level": account[0].level
                },
                {
                    "email": account[1].email,
                    "password": account[1].password,
                    "type": account[1].type,
                    "details": account[1].details,
                    "credit_score": account[1].credit_score,
                    "loan_balance": account[1].loan_balance,
                    "user_info": account[1].user_info,
                    "level": account[1].level,
                    "transactions": account[1].transactions,
                    "date_opened": account[1].date_opened
                }
            ])

            data = json.dumps(data, indent=4)
            with open("accounts.json", "w") as file:
                file.write(data)
            return

    # If account we are saving doesn't exist
    data.append([
        {
            "email": account[0].email,
            "password": account[0].password,
            "type": account[0].type,
            "details": account[0].details,
            "balance": account[0].balance,
            "user_info": account[0].user_info,
            "level": account[0].level
        },
        {
            "email": account[1].email,
            "password": account[1].password,
            "type": account[1].type,
            "details": account[1].details,
            "credit_score": account[1].credit_score,
            "loan_balance": account[1].loan_balance,
            "user_info": account[1].user_info,
            "level": account[1].level,
            "transactions": account[1].transactions,
            "date_opened": account[1].date_opened
        }
    ])

    data = json.dumps(data, indent=4)
    with open("accounts.json", "w") as file:
        file.write(data)


if __name__ == "__main__":
    new_account = CheckingsAccount(level=3, password="testing123$@()4",
                                   user_info=["Daniel Fabusuyi", "1532 Transit Parkway", 35],
                                   email="folajimifabusuyi@gmail.com")
    new_account2 = CreditAccount(level=3, password="testing123$@()4",
                                 user_info=["Daniel Fabusuyi", "1532 Transit Parkway", 35],
                                 email="folajimifabusuyi@gmail.com")
    save_account([new_account, new_account2])