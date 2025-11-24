def safe_divide(a, b):
    try:
        result = a / b
        return result
    # except:
    #     print("cannot divide by zero")
    #     return None
    except ZeroDivisionError:
        print("Cannot devide by zero!")
        return None
    except TypeError:
        print("Not a valid number!")
        return None
    except:
        print("An error has occured!")
    
# print(safe_divide(10, 2)) # 5.0
# print(safe_divide(10, 0)) # Cannot devide by zero! None
# print(safe_divide(10, "hello")) # Not a valid number! None

def safe_operations(a, b, lst, key, d):
    try:
        print(f"Division result: {a/b}") # ZeroDivisionError, TypeError
        print("Access list elemnet:", lst[2]) # IndexError
        print("Access dictionary key:", d[key]) # KeyError
        print(f"Add numbers: {a + b}") # TypeError
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except IndexError:
        print("List index out of range!")
    except KeyError:
        print(f"Key {key} not found in dictionary!")
    except TypeError:
        print("Invalid types for operation!")
    except Exception as e:
        print("Some other error occured", e)
        
print(safe_operations(10, 2, [1, 2], "Tom", {"John": 15}))

# Practice problems

def calculate_price_per_item(total_cost, num_items):
    try:
        price_per_item = total_cost / num_items
        return round(price_per_item, 2)
    except ZeroDivisionError:
        print("No items to calculate")
    
print(calculate_price_per_item(200, 4))
print(calculate_price_per_item(50, 0))
print(calculate_price_per_item(25.50, 3))

def parse_age(age):
    try:
        return int(age)
    except ValueError:
        return None

print(parse_age("007"))
print(parse_age("25.5"))