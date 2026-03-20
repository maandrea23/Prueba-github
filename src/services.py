# Importing validations
from validations import validate_int_over_0, validate_not_empty, validate_type_of_operation
# Creating provitional list to work the functions
operations = []
balance = 0
# Function for income uses validations on the valitadions file and adds the values to a local dictionary to add this dictionary to the list operations
def income(operations, balance):
    value = validate_int_over_0("Insert your income please: ")
    concept = validate_not_empty("Insert the concept of the income: ")
    balance = balance + value
    local_dictionary = {}
    local_dictionary["value"] = value
    local_dictionary["concept"] = concept
    local_dictionary["type"] = "Income"
    operations.append(local_dictionary)
    return balance

# Function for outcome uses validations on the valitadions file and adds the values to a local dictionary to add this dictionary to the list operations
def outcome(operations, balance):
    value = validate_int_over_0("Insert your outcome please: ")
    if value> balance:  
        concept = validate_not_empty("Insert the concept of the outcome: ")
        balance = balance - value
        local_dictionary = {}
        local_dictionary["value"] = -value
        local_dictionary["concept"] = concept
        local_dictionary["type"] = "outcome"
        operations.append(local_dictionary)
        return balance
    else:
        print("You don't have enough balance to have this outcome") 

# Function to show the movements contened in the list operations
def show_movements(operations):
    index = 1
    for operation in operations:
        print(f"{index}. {list(operation.values())}")
        index+=1

def edit_movements(operations, balance):
    show_movements(operations)
    index= len(operations)
    while True:
        operation_to_edit = validate_int_over_0("Insert the number of the operation to edit: ") -1
        if operation_to_edit> index:
            print(f"Select a number between 1 and {index}")
        else:
            break

    type_of_operation = validate_type_of_operation("Insert 1 for income or 2 for outcome")
    if type_of_operation ==1:
        value = validate_int_over_0("Insert your income please: ")
        concept = validate_not_empty("Insert the concept of the income: ")
        current_value = operations[operation_to_edit]["value"]
        balance = balance + value - current_value
        operations[operation_to_edit]["value"] = value
        operations[operation_to_edit]["concept"] = concept
        operations[operation_to_edit]["type"] = "income"
    else:
        value = validate_int_over_0("Insert your outcome please: ")
        if value> balance:  
            concept = validate_not_empty("Insert the concept of the outcome: ")
            balance = balance - value - current_value
            operations[operation_to_edit]["value"] = -value
            operations[operation_to_edit]["concept"] = concept
            operations[operation_to_edit]["type"] = "income"
        else:
            print("You don't have enough balance to have this outcome, returning to menu...") 
            return
    return balance





for i in range (2):
    balance=income(operations, balance)

print(f"Total balance: ${balance}")

balance = edit_movements(operations, balance)

print(f"Final edited balance: ${balance}")
