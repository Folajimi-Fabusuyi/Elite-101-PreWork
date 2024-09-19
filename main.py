def print_menu():
    global username
    print(f"How may I help you {username}:")
    print("\t1. -- Placeholder Option --")
    print("\t2. -- Placeholder Option --")
    print("\t3. -- Placeholder Option --")
    print("\t4. -- End Conversation --")

    choice = input("Enter the number associated with your choice: ")
    while not choice.isdigit() or (int(choice) > 4 or int(choice) < 1):
        print("\tPlease input a valid number")
        choice = input("\nEnter the number associated with your choice: ")

    return int(choice)


# Welcome Sequence
print("Welcome to the Elite 101 Chatbot, I am at your service.")
print("Before we begin, some basic information is needed.")


# User info gathering process.
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

# Menu
while True:
    choice = print_menu()
    if choice == 4:
        print(f"Signing out user: {username}")
        print("Have a great day!")
        break
    else:
        continue
