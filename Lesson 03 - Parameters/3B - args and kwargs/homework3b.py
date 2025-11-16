# Question 1

def combine_values(*nums):
    mult = 1
    if not nums:
        return mult
    for num in nums:
        mult *= num
    return mult

print(combine_values(2, 3, 4))
print(combine_values(5))
print(combine_values())

# Question 2

def merge_details(label, **kwargs):
    dict = {"label": label}
    dict.update(kwargs) # i didn't understand this one thing - .update()
    return dict

print(merge_details("ItemA", size="Large", cost=12.50))
print(merge_details("UserX"))

# Question 3 - Tracing

# Output1: 8
# Output2: 10
# Output3: 0

# Question 4 - Tracing

# Ouput1: {"Alpha", "x": 1, "y": 2, "count": 2}
# Ouput2: {"Beta", "count": 0}