import random, getpass
import password_functions as pswd

# {Account LVL: ["Account Rank", LVL Balance Drain, Interest Rate]}
ACCOUNT_DETAILS = {
    0: {"rank": "Basic", 
        "balance_drain": 0, 
        "interest_rate": 1.01},
    1:{"rank": "Economy", 
        "balance_drain": 1000, 
        "interest_rate": 1.08},
    2: {"rank": "Premium", 
        "balance_drain": 2500, 
        "interest_rate": 1.1},
    3: {"rank": "VIP", 
        "balance_drain": 4000, 
        "interest_rate": 1.15}
}


class Account:

    def __init__(self, email="none", password=["none", 000], type="Checkings", level=0, user_info=["name", "address", "age"]):
        self.email = email
        self.password = password
        self.type = type

        if self.type == "Credit":
            self.credit_init()
        else:
            self.checkings_init(level)

        self.user_info = user_info

    def checkings_init(self, level):
        self.balance = 0
        self.details = ACCOUNT_DETAILS[level]

    def deposit_money(self, amount):
        if self.type == "Checkings":
            self.balance += amount

    def update_account(self):
        if self.type == "Checkings":
            self.balance *= self.details["interest_rate"]
            self.balance -= self.details["balance_drain"]
            if self.balance < 0:
                self.balance = 0
                self.details = ACCOUNT_DETAILS[0]

    def __str__(self):
        return (f"\nName: {self.user_info[0]}\nAddress: {self.user_info[1]}\nAge: {self.user_info[2]}\nEmail: {self.email}\nAccount Type: {self.type}\nBalance: {self.balance}" +
        f"\nAccount Rank: {self.details['rank']}\n\tDrain: {self.details['balance_drain']}\n\tInterest Rate: {self.details['interest_rate']}\n\tPassword: {self.password}")


def create_account():
    print("You will now begin the account creation process")
    email = input("Email: ")
    password = pswd.encrypt_password(getpass.getpass("Password: "))
    user_info = [input("Name: "), input("Address: "), input("Age: ")]
    type = None
    while type not in ["Checkings", "Credit"]:
        type = input("Account Type [Checkings or Credit]: ").capitalize()

    return Account(email=email, password=password, user_info=user_info, type=type)
            
    

if __name__ == "__main__":
    # new_account = Account(level=3, password="testing123$@()4", user_info=["Daniel Fabusuyi", "1532 Transit Parkway", 35], email="folajimifabusuyi@gmail.com")
    new_account = create_account()
    print(new_account)
    print(pswd.decrypt_password(new_account.password))