# Importing validations
from validations import validate_positive_int, validate_not_empty, validate_type_of_operation

# Function for income: adds to operations and balance
def income(operations, balance):
    value = validate_positive_int("Insert your income please: ")
    concept = validate_not_empty("Insert the concept of the income: ")
    balance += value
    operation = {
        "value": value,
        "concept": concept,
        "type": "Income"
    }
    operations.append(operation)
    print(f"Income registered. New balance: ${balance}")
    return balance

# Function for outcome: checks balance first
def outcome(operations, balance):
    value = validate_positive_int("Insert your outcome please: ")
    if value > balance:
        print("You don't have enough balance for this outcome.")
        return balance
    concept = validate_not_empty("Insert the concept of the outcome: ")
    balance -= value
    operation = {
        "value": -value,
        "concept": concept,
        "type": "Outcome"
    }
    operations.append(operation)
    print(f"Outcome registered. New balance: ${balance}")
    return balance

# Show movements
def show_movements(operations):
    if not operations:
        print("No movements yet.")
        return
    print("\nMovements:")
    for i, op in enumerate(operations, 1):
        if op["value"] > 0:
            sign = "+"  
        else:
            sign = "-"
        print(f"{i}. {op['type']}: {sign}${abs(op['value'])} - {op['concept']}")

# Edit movement
def edit_movements(operations, balance):
    show_movements(operations)
    n= len(operations)
    while True:
        operation_to_edit = validate_positive_int("Insert the number of the operation to edit: ") -1
        if operation_to_edit> n:
            print(f"Select a number between 1 and {n}")
        else:
            break

    type_of_operation = validate_type_of_operation("Insert 1 for income or 2 for outcome")
    if type_of_operation ==1:
        value = validate_positive_int("Insert your income please: ")
        concept = validate_not_empty("Insert the concept of the income: ")
        current_value = operations[operation_to_edit]["value"]
        balance = balance + value - current_value
        operations[operation_to_edit]["value"] = value
        operations[operation_to_edit]["concept"] = concept
        operations[operation_to_edit]["type"] = "income"
    else:
        value = validate_positive_int("Insert your outcome please: ")
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

# Delete operation
def delete_operation(operations, balance):
    show_movements(operations)
    n= len(operations)
    while True:
        operation_to_delete = validate_positive_int(f"Select a number between 1 and {n} to delete: ") -1
        if operation_to_delete> n:
            print(f"Select a number between 1 and {n}")
        else:
            break
    operation_deleted = operations.pop(operation_to_delete)
    current_value= operation_deleted["value"]
    balance = balance - current_value
    return balance

