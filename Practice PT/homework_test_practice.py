# QUESTION 15
# Find and fix the error in the code:
# Original code:
# def calculate_average(numbers):
#     total = sum(numbers)
#     average = total / len(numbers)
#     return average

# grade = []
# result = calculate_average(grade)
# print(f"Average: {result}")

# The error is that there's no edge case - if this code is run, it will prind an error because grade is empty.
# Fixed version:

def calculate_average(numbers):
    if not numbers:
        return 0
    total = sum(numbers)
    average = total / len(numbers)
    return average

grade = []
result = calculate_average(grade)
print(f"Average: {result}")

# QUESTION 16
# Answer: C) required --> *args --> defaults --> **kwargs

# QUESTION 17
# First blank: strip
# Second blank: upper
# Third blank: split
# Fourth blank: len

# QUESTION 18
def validate_password(password):
    if not password:
        return False, "Empty password"
    if len(password) >= 8:
        return True, "Valid"
    return False, "Too short"

print(validate_password(""))
print(validate_password("abc"))
print(validate_password("secure123"))

# QUESTION 19
def create_inventory(item_name, *quantities, location="Warehouse"):
    total = sum(quantities)
    if not quantities:
        total = 0
    return {
        "item": item_name,
        "total": total,
        "location": location
    }
    
print(create_inventory("Widget", 10, 20, 15))
print(create_inventory("Gadget", 5, location="Store"))
print(create_inventory("Phone", location="Shipping Facility"))

# QUESTION 20
def safe_list_access(items, index):
    try:
        item = items[index]
        return item, True
    except IndexError:
        return None, False
        
print(safe_list_access([10, 20, 30], 1))
print(safe_list_access([10, 20, 30], 10))
print(safe_list_access([], 0))