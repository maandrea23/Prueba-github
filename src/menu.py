from validations import validate_option                  
balance=0
def show_menu():
    while True:
        print("\n\t.:MENU:.")
        print(f"This is your current balance: ${balance}")
        print("\n1. Register income")
        print("2. Register outcome")
        print("3. View operations")
        print("4. Edit operation")
        print("5. Delete operation")
        print("6. Exit")
        option = validate_option()
    
        if option == 1:
            print("💰")
        elif option == 2:
            print("💸") 
        elif option == 3:
            print("👀")
        elif option == 4:
           print()
        elif option == 5:
            print()
        elif option == 6:
            print("See you soon!!! 👋🏻")
            break
        else:
            print("Invalid option ❌ \nInsert a valid option.")

show_menu()


