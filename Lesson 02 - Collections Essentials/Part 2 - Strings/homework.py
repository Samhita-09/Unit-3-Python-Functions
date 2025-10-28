# Question 1

# Output: john.smith gmail.com
# Explanation: The normalized variable converts the email to full lowercase, then the username splits it where the @ symbole is, creating a list and selecting index 0 which is the first element. The domain variable then selects the second element of the normalized list, and then the username and domain are printed.

# Question 2

# Output: tqbf
# Explanation: The words variable splits the text wherever there's a space. Initials is originally an empty string, and the for loop that comes after it selects the first letter of each word and makes them lowercase. These lowercase letters are added into the initials string, and that's what is printed.

# Question 3

def extract_domain(email):
    count = email.count("@")
    if count != 1:
        return "Invalid email"
    return email.lower().split("@")[1]

print(extract_domain("john@gmail.com"))
print(extract_domain("JANE@YAHOO.COM"))
print(extract_domain("missing.at.sign.com"))
print(extract_domain("too@@many@signs.com"))

# Question 4

# Output: 123456
# Explanation: A variable, digits, is set as an empty string initially. A for loop is used to iterate through each character in the message and check if they are a number. If the character is a number, it's added to the string and that string is printed.

# Question 5

# Output: MY_DOCUMENT
# Explanation: The variable name_only is used to replace the ending, ".txt" with a space, and then safe_name is used to replace the dash in the filename with an underscore. Result is then used to make the whole filename uppercase, and that is printed.

# Question 6

# Output: banana
# Explanation: Items is used to make the data into a list, splitting up the variable wherever there's a comma. Longest is initially set to the first item of the list, and then there's a for loop used to look at the length of each item. If the length of the item the loop is checking is longer than the "longest" variable, that item becomes the longest variable. This is what's printed.

# Question 7

def filter_numbers(text):
    new = ""
    for char in text:
        if not char.isdigit():
            new += char
    return new

print(filter_numbers("Hello123World456"))
print(filter_numbers("Test 1 2 3"))
print(filter_numbers("Price: $29.99"))
print(filter_numbers("No numbers here!"))

# Question 8

# Output: htps//example.com/users/profile
# Explanation: The parts variable is used to split up the url wherever there's a slash. Protocol is used to select the first item of that list and domain is used to select the third item, "example.com". Path is then used to combine the last two items of the list -- users and profile with a slash between them. All variables are then printed in an f string with a slash separating each of them.

# Question 9

def count_character_types(text):
    num_letters = 0
    num_digits = 0
    num_spaces = 0
    for char in text:
        if char.isdigit():
            num_digits += 1
        elif char == " ":
            num_spaces += 1
        elif char.isalpha():
            num_letters += 1
    return f"Letters: {num_letters}, Digits: {num_digits}, Spaces: {num_spaces}"

print(count_character_types("Hello 123"))
print(count_character_types("Test2024!"))