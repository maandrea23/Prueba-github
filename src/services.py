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
        sign = "+" if op["value"] > 0 else "-"
        print(f"{i}. {op['type']}: {sign}${abs(op['value'])} - {op['concept']}")

# Edit movement
def edit_movements(operations, balance):
    if not operations:
        print("No movements to edit.")
        return balance
    show_movements(operations)
    n = len(operations)
    while True:
        idx = validate_positive_int(f"Enter number (1-{n}) to edit: ") - 1
        if 0 <= idx < n:
            break
        print(f"Select between 1 and {n}")
    
    type_op = validate_type_of_operation("1 for income, 2 for outcome: ")
    value = validate_positive_int("Enter new value: ")
    concept = validate_not_empty("Enter new concept: ")
    
    current_value = operations[idx]["value"]
    delta = value if type_op == 1 else -value
    new_balance = balance + delta - current_value
    
    # Check if outcome exceeds balance
    if type_op == 2 and value > new_balance:
        print("Not enough balance for this outcome.")
        return balance
    
    operations[idx] = {
        "value": delta,
        "concept": concept,
        "type": "Income" if type_op == 1 else "Outcome"
    }
    print(f"Operation edited. New balance: ${new_balance}")
    return new_balance

# Delete operation
def delete_operation(operations, balance):
    if not operations:
        print("No movements to delete.")
        return balance
    show_movements(operations)
    n = len(operations)
    while True:
        idx = validate_positive_int(f"Enter number (1-{n}) to delete: ") - 1
        if 0 <= idx < n:
            break
        print(f"Select between 1 and {n}")
    
    deleted = operations.pop(idx)
    balance -= deleted["value"]  # Since value is negative for outcome, adds back
    print(f"Operation deleted. New balance: ${balance}")
    return balance

