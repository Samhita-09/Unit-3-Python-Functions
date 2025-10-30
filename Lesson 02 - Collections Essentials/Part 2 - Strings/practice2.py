# Question 3

def format_phone_number(phone):
    digits = phone.replace("-", "").replace(" ", "").replace("(", "").replace(")", "")
    if len(digits) != 10 or not digits.isdigit():
        return "Invalid phone number"
    chunk1 = digits[0:3]
    chunk2 = digits[3:6]
    chunk3 = digits[6:]
    return f"({chunk1}){chunk2}-{chunk3}"

print(format_phone_number("555-123-4567"))
print(format_phone_number("(555) 123 4567"))
print(format_phone_number("5551234567"))
print(format_phone_number("123"))