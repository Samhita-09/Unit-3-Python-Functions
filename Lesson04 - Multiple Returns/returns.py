# The Tricky Trio: None vs False vs 0

def search_data(query):
    if query == "":
        return None # No query provided
    if query == "empty":
        return 0 # Found zero results
    if query == "error":
        return False # Search failed
    return len(query) # Normal case - return count

# Return Type - None -> "No Value"
# Meaning: Absense of value, not set, not found
# Use for: Missing data, search failures, optional parameters
result = None
print(result is None) # True - Identity check
print(result == None) # True - Equality check
print(not result) # True - Falsy check

# 2 Return Type - False
# Meaning: Explicit false condition, validation failur, negative result
# Use for: Validation result, boolean operations, success/failure status
result = False
print(result is False) # True - identity check
print(not result) # True - boolean negation
print(result == 0) # True - falsy check

# Return Zero - A Valid Number
# Zero is a VALID numerical value, not the absense of a value
result = 0
print(result == 0) # True - numeric equality
print(not result) # True - falsy in boolean context
print(result is None) # False - different objects
print(result is False) # False - different types