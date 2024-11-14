import datetime as dt
import math
import random

from password_functions import encrypt_password

# \033[0m --> \033 is the string customization escape charachter [(number)m is the specific rule for the string
# {Account LVL: ["Account Rank", LVL Balance Drain, Interest Rate]}
CHECKINGS_ACCOUNT_DETAILS = {
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

CREDIT_ACCOUNT_DETAILS = {
    0: {"rank": "Basic",
        "credit_increment": 1,
        "credit_requirement": 0},
    1: {"rank": "Economy",
        "credit_increment": 2,
        "credit_requirement": 650},
    2: {"rank": "Premium",
        "credit_increment": 3,
        "credit_requirement": 700},
    3: {"rank": "VIP",
        "credit_increment": 4,
        "credit_requirement": 750}
}


class CheckingsAccount:

    def __init__(self, email="none", password="Default", level=0, user_info=("name", "address", "age"), balance=0):
        self.email = email
        self.password = encrypt_password(password)
        self.type = "Checkings"
        self.checkings_init(level, balance)
        self.user_info = user_info

        self.level = level

    def checkings_init(self, level, balance):
        self.balance = balance
        self.details = CHECKINGS_ACCOUNT_DETAILS[level]

    def deposit_money(self, amount):
        self.balance += amount

    def update_account(self):
        self.balance *= self.details["interest_rate"]
        self.balance -= self.details["balance_drain"]
        if self.balance < 0:
            self.balance = 0
            self.details = CHECKINGS_ACCOUNT_DETAILS[0]
            self.level = 0

    def __str__(self):
        return (f"\033[95m---------------------------------------------------------------------------\033[0m\n"
                f"\033[98m\033[1mAccount Info:"
                f"\n\t\033[1m• Name:\033[0m {self.user_info[0]}"
                f"\n\t\033[1m• Address:\033[0m {self.user_info[1]}"
                f"\n\t\033[1m• Age:\033[0m {self.user_info[2]}"
                f"\n\t\033[1m• Email:\033[0m {self.email}"
                f"\n\t\033[1m• Password:\033[0m {len(self.password[0]) * '*'}"
                f"\n\t\033[1m• Type:\033[0m {self.type}"
                f"\n\033[92m\033[1mBalance:\033[0m {self.balance}" +
                f"\n\033[93m\033[1mAccount Level:\033[0m {self.level}"
                f"\n\t\033[1m• Rank:\033[0m {self.details['rank']}"
                f"\n\t\033[1m• Drain:\033[0m -${self.details['balance_drain']}"
                f"\n\t\033[1m• Interest Rate:\033[0m {self.details['interest_rate']}%"
                f"\033[95m\n---------------------------------------------------------------------------\033[0m")

# TODO: Optional: Add onto Credit Account methods as needed
class CreditAccount:

    def __init__(self, email="none", password="Default", level=0, user_info=("name", "address", "age"), date_opened=dt.datetime.now().strftime("%m/%d/%Y - %I:%M:%S %p"), credit_score=random.randint(600, 650), loan_balance=0, transactions=[]):
        self.email = email
        self.password = encrypt_password(password)
        self.type = "Credit"
        self.credit_init(level, date_opened, credit_score, loan_balance, transactions)
        self.user_info = user_info

        self.level = level
        self.transactions = []

    def credit_init(self, level, date_opened, credit_score, loan_balance, transactions):
        self.date_opened = date_opened
        self.details = CREDIT_ACCOUNT_DETAILS[level]
        self.credit_score = credit_score
        self.loan_limit = math.floor(7500 * math.exp(0.0071 * (self.credit_score - 600)))
        self.loan_balance = loan_balance

        self.transactions = transactions

    def credit_score_update(self, status="upgrade"):
        if status == "upgrade": self.credit_score += math.floor(self.credit_score * 0.005) + (self.details["credit_increment"])
        elif status == "downgrade": self.credit_score -= math.floor(self.credit_score * 0.005) + (self.details["credit_increment"])

    def update_account(self):
        self.loan_limit = math.floor(7500 * math.exp(0.0071 * (self.credit_score - 600)))
        if  self.credit_score < self.details["credit_requirement"]:
            self.level -= 1
        elif self.level != 3:
            if self.credit_score >= CREDIT_ACCOUNT_DETAILS[self.level + 1]["credit_requirement"]:
                self.level += 1

        if self.level < 0: self.level = 0
        self.details = CREDIT_ACCOUNT_DETAILS[self.level]

    def __str__(self):
        return (f"\033[95m---------------------------------------------------------------------------\033[0m\n"
                f"\033[98m\033[1mAccount Info:"
                f"\n\t\033[1m• Name:\033[0m {self.user_info[0]}"
                f"\n\t\033[1m• Address:\033[0m {self.user_info[1]}"
                f"\n\t\033[1m• Age:\033[0m {self.user_info[2]}"
                f"\n\t\033[1m• Email:\033[0m {self.email}"
                f"\n\t\033[1m• Password:\033[0m {'*' * len(self.password[0])}"
                f"\n\t\033[1m• Type:\033[0m {self.type}"
                f"\n\033[92m\033[1mCredit Score:\033[0m {self.credit_score}"
                f"\n\033[93m\033[1mAccount Level:\033[0m {self.level}"
                f"\n\t\033[1m• Rank:\033[0m {self.details['rank']}"
                f"\n\t\033[1m• Credit Score Increment:\033[0m +{self.details['credit_increment']}"
                f"\n\t\033[1m• Loan Limit:\033[0m ${self.loan_limit}"
                f"\n\033[91m\033[1mLoan Balance: -${self.loan_balance}"
                f"\033[95m\n---------------------------------------------------------------------------\033[0m")

