from validations import validate_option, validate_type_of_operation, validate_not_empty     
from services import income, outcome,show_movements, edit_movements, delete_operation         
balance=0
def show_menu(operations, balance):
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
            balance = income(operations, balance)
        elif option == 2:
            print("💸") 
        elif option == 3:
            print("👀")
        elif option == 4:
           print()
        elif option == 5:
            print()
        elif option == 6:

            break
        else:
            print("Invalid option ❌ \nInsert a valid option.")

show_menu()


