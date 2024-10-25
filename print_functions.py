def print_menu(username):
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
