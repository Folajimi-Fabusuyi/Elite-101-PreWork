import json
from account_functions import *

def save_account(account: Account):
    if account.type == "Checkings":
        data = {
            "email": account.email,
            "password": account.password,
            "type": account.type,
            "details": account.details,
            "balance": account.balance,
            "user_info": account.user_info,
            }
    else:
        pass

    data = json.dumps(data, indent=4)
    
    with open("accounts.json", "w") as file:
        file.write(data)

if __name__ == "__main__":
    new_account = Account(level=3, password="testing123$@()4", user_info=["Daniel Fabusuyi", "1532 Transit Parkway", 35], email="folajimifabusuyi@gmail.com")
    save_account(new_account)