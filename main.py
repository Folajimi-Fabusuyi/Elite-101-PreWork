def print_menu():
    global username
    print(f"How may I help you {username}:")
    print("\t1. -- My Data --")
    print("\t2. -- My Transcript --")
    print("\t3. -- My To-do's --")
    print("\t4. -- End Conversation --")

    choice = input("Enter the number associated with your choice: ")
    while not choice.isdigit() or (int(choice) > 4 or int(choice) < 1):
        print("\tPlease input a valid number")
        choice = input("\nEnter the number associated with your choice: ")

    return int(choice)

def print_choice(choice):
    if choice == 1:
        print("\n+-----Data-----+")
        print(f"Name: {username}")
        print(f"Age: {age}")
        print("Session Time: null\n")
    elif choice == 2:
        print(f"\n+-----Transcript-----+")
        print("Grade: 11")
        print("GPA Unweighted: 4.0")
        print("GPA Weighted: 5.2")
        print("Rank: 50/2679")
        print("Graduation Year: 2026\n")
    elif choice == 3:
        print("\n+-----Todos-----+")
        print("1. Replace placeholders")
        print("2. Turn into Object Oriented Program")
        print("3. Make Chatbot more flexible\n")
    else:
        print(f"Signing out user: {username}")
        print("Have a great day!")
        return False
    return True


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
in_loop = True
while in_loop:
    choice = print_menu()
    in_loop = print_choice(choice)
