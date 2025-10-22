# Question 3

def calculate_discount(price, member_status):
    if member_status == "premium":
        discounted_price = 0.7 * price
        return discounted_price
    elif member_status == "standard":
        discounted_price = 0.85 * price
        return discounted_price
    else:
        return price
    
final_price = print(f"Price: {calculate_discount(100, "premium")}") # 70.0
final_price = print(f"Price: {calculate_discount(100, "standard")}") # 85.0
final_price = print(f"Price: {calculate_discount(100, "guest")}") # 100

# Question 6

def count_vowels(text):
    vowel_count = 0
    for char in text:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            vowel_count += 1
        if char == "A" or char == "E" or char == "I" or char == "O" or char == "U":
            vowel_count += 1
    return vowel_count

print(f"Vowels in text: {count_vowels("Hello World")}")
print(f"Vowels in text: {count_vowels("Python")}")
print(f"Vowels in text: {count_vowels("AEIOU")}")

# Alternative way

def count_vowels1(text):
    '''Count Vowels in text (case insensitive).'''
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# Question 9

def validate_password(password):
    len_valid = False
    has_digit = False
    if len(password) >= 8:
        len_valid = True
    for char in password:
        if '0' <= char <= '9':
            has_digit = True
    if has_digit and len_valid:
        return True
    else:
        return False
    
print(validate_password("Samhita09"))