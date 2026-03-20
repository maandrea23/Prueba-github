def validate_int_over_0(message):
    while True:
        try:
            value = int(input(message))
            if value<=0:
                print("Invalid input, please enter an integer.")
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
            if option > 0 and option <= 6:
                print("Option validate :)")
                break
            else: 
                print("select valid option")
        except ValueError:
            print("Invalid option, pelase try again")

def validate_type_of_operation(message):
    while True:
        try:
            type_of_operation = int(input(message))
            if type_of_operation > 2 and type_of_operation <1:
                print("Invalid number")
            else:
                return type_of_operation
        except ValueError:
            print("Invalid number")