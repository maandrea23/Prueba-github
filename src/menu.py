from validations import validate_option
from services import income, outcome, show_movements, edit_movements, delete_operation  


def show_menu(operations, balance):
    while True:
        print("\n\t.:MENU:.")
        print(f"Your current balance: ${balance}")
        print("1. Register income")
        print("2. Register outcome") 
        print("3. View movements")
        print("4. Edit operation")
        print("5. Delete operation")
        print("6. Exit")
        option = validate_option()
    
        if option == 1:
            balance = income(operations, balance)
        elif option == 2:
            balance = outcome(operations, balance)
        elif option == 3:
            show_movements(operations)
        elif option == 4:
            balance = edit_movements(operations, balance)
        elif option == 5:
            balance = delete_operation(operations, balance)
        elif option == 6:
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")
    return balance
