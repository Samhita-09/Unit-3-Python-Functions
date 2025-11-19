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



# Multiple Returns - python packs multiple returns into a tuple
def calculate_room(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter # returns a tuple (area, perimeter)

print(calculate_room(10, 5))
print(type(calculate_room(10, 5)))

print(type((42))) # int
print(type((42,))) # tuple for single item
# print(type(1, 2, 3)) # doesnt work
no_parentheses = 1, 2, 3
print(type(no_parentheses)) # tuple

# unpacking tuple
area_result, perimeter_result = calculate_room(20, 6)
print(f"Area: {area_result}")
print(f"Perimeter: {perimeter_result}")

# Practice 1 - Student Analyzer

def analyze_grades(grades):
    if not grades:
        return 0, 0, 0, False
    avg = sum(grades) / len(grades)
    highest = 0
    lowest = 100
    passed = True
    for grade in grades:
        if grade > highest:
            highest = grade
        if grade < lowest:
            lowest = grade
        if avg < 60:
            passed = False
    return avg, highest, lowest, passed

# Mr. Gemici's Way - More Efficient
# def analyze_grades(grades):
#     if not grades:
#         return 0, 0, 0, False
#     avg = sum(grades) / len(grades)
#     highest = max(grades)
#     lowest = min(grades)
#     passed = avg >= 60
    

print(analyze_grades([80, 80, 80]))
print(analyze_grades([85, 92, 78, 90]))
print(analyze_grades([]))