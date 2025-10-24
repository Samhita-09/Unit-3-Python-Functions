# Question 3

num_input = input("Enter a list of numbers: ")
num_list = []

for num in num_input:
    number = int(num)
    num_list.append(number)
print(f"Your numbers list: {num_list}")

def filter_evens(num_list):
    evens = []
    for numbers1 in num_list:
        if numbers1 % 2 == 0:
            evens.append(numbers1)
    return evens
            
print(f"The even numbers you entered are: {filter_evens(num_list)}")

# Question 6

def list_stats(numbers):
    new_list = []
    if numbers:
        total = sum(numbers)
        avg = total/(len(numbers))
        minimum = min(numbers)
        maximum = max(numbers)
        new_list.append(minimum)
        new_list.append(maximum)
        new_list.append(avg)
        return(new_list)
    else:
        return None
    
print(list_stats([10, 20, 30, 40]))
print(list_stats([]))