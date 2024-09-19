print("Welcome to the Elite 101 Chatbot, I am at your service.")
print("Before we begin, some basic information is needed.")

confirmation = False
while not confirmation:
    username = input("\n\tEnter your name: ")
    age = input("\tEnter your age: ")
    while not age.isdigit():
        print("\tPlease input a number")
        age = input("\n\tEnter your age: ")
    age = int(age)

    while True:
        confirmation = input(f"\nWelcome {username}! Your age is {age}. Is this information correct? [Y/N]: ")

        if confirmation.lower() in ["yes", "y"]:
            confirmation = True
            break
        elif confirmation.lower() in ["no", "n"]:
            confirmation = False
            break
        else:
            print("Invalid option")
