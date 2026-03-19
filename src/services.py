#Importing validations
from validations import validate_int_over_0, validate_not_empty
#Creating provitional list to work the functions
operations = []
#Function for income uses validations on the valitadions file and adds the values to a local dictionary to add this dictionary to the list operations
def income(operations):
    value = validate_int_over_0("Insert your income please: ")
    concept = validate_not_empty("Insert the concept of the income: ")
    local_dictionary = {}
    local_dictionary["value"] = value
    local_dictionary["concept"] = concept
    local_dictionary["type"] = "Income"
    operations.append(local_dictionary)

#Function for outcome uses validations on the valitadions file and adds the values to a local dictionary to add this dictionary to the list operations
def outcome(operations):
    value = validate_int_over_0("Insert your outcome please: ")
    concept = validate_not_empty("Insert the concept of the outcome: ")
    local_dictionary = {}
    local_dictionary["value"] = -value
    local_dictionary["concept"] = concept
    local_dictionary["type"] = "outcome"
    operations.append(local_dictionary)



print(operations)