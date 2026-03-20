
def validate_positive_int(message):
    while True:
        try:
            value = int(input(message))
            if value <= 0:
                print("Invalid input, please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input, please enter an integer.")

def validate_not_empty(message):
    while True:
        try:
            concept = input(message)
            if concept != "":
                return concept
            else:
                print("Please write something")
        except ValueError:
            print("Please write something")
            
def validate_option():
    while True:
        try:
            option = int(input("Select an option: "))
            if 1 <= option <= 6:
                return option
            else: 
                print("Select a valid option")
        except ValueError:
            print("Invalid option, please try again")

def validate_type_of_operation(message):
    while True:
        try:
            type_of_operation = int(input(message))
            if type_of_operation == 1 or type_of_operation == 2:
                return type_of_operation
            else:
                print("Invalid number. Select 1 for income or 2 for outcome.")
        except ValueError:
            print("Invalid number")

