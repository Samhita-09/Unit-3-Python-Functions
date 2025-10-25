# Problem 1

def remove_duplicates(items):
    no_doubles = []
    if not items:
        return "Please input a valid list."
    for item in items:
        if item not in no_doubles:
            no_doubles.append(item)
    return no_doubles

print(remove_duplicates([1, 2, 2, 3, 1, 4]))
print(remove_duplicates(["a", "b", "a", "c"]))
print(remove_duplicates([5, 5, 5]))
print(remove_duplicates([]))

# Problem 2

def find_common(list1, list2):
    common = []
    if not list1:
        return "Please enter a valid list1"
    elif not list2:
        return "Please enter a valid list2"
    for item in list1:
        if item in list2 and item not in common:
            common.append(item)
    return common

print(find_common([1, 2, 3], [2, 3, 4]))
print(find_common(["a", "b", "c"], ["c", "d"]))
print(find_common([1, 1, 2], [2, 2, 3]))
print(find_common([], [1, 2]))

# Problem 3

def reverse_sublists(data, size):
    reversed = []
    for i in range(0, len(data), size):
        chunk = data[i:i+size]
        reversed.extend(chunk[::-1])
    return reversed

print(reverse_sublists([1, 2, 3, 4, 5, 6], 2))

# Problem 4

def rotate_list(items, positions):
    rotated = []
    if positions == 0:
        return items
    if abs(positions) > len(items):
        positions = positions % len(items)
    rotated.extend(items[-positions:] + items[0:-positions])
    return rotated

print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], -2))
print(rotate_list([1, 2, 3], 0))
print(rotate_list([1, 2, 3], 5))