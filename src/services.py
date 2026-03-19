#Importing validations
from validations import validate_int_over_0, validate_not_empty
#Creating provitional list to work the functions
operations = []
balance = 0
#Function for income uses validations on the valitadions file and adds the values to a local dictionary to add this dictionary to the list operations
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

#Function for outcome uses validations on the valitadions file and adds the values to a local dictionary to add this dictionary to the list operations
def outcome(operations, balance):
    value = validate_int_over_0("Insert your outcome please: ")
    concept = validate_not_empty("Insert the concept of the outcome: ")
    balance = balance - value
    local_dictionary = {}
    local_dictionary["value"] = -value
    local_dictionary["concept"] = concept
    local_dictionary["type"] = "outcome"
    operations.append(local_dictionary)
    return balance


for i in range (3):
    balance=income(operations, balance)
print(operations)
print("Balance final: ", balance)