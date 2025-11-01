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

# Question 6

# Group 1 idea
def sanitize_filename(filename):
    a = filename.replace(" ", "_").lower()
    for char in a:
        if not char.isalpha() and not char.isdigit():
            if char not in ".-_":
                a.replace(char, "")
    if not a.endswith(".txt"):
        a = a + ".txt"
    if len(a) > 50:
        return "Invalid - must not exceed 50 characters"
    return a

print(sanitize_filename("Ancient Scroll.txt"))
print(sanitize_filename("Quest 2042! (Epic)"))
print(sanitize_filename("notes"))
print(sanitize_filename("X" * 60))

# Alternative Method #1

def sanitize_filename(filename):
    clean = filename.lower()
    clean = clean.replace(" ", "_")
    allowed = ""
    for char in clean:
        if char.isalnum() or char in ".-_":
            allowed += char
    if allowed.endswith(".txt"):
        result = allowed
    else:
        if "." in allowed:
            dot_pos = allowed.rfind(".")
            allowed = allowed[:dot_pos]
        result = allowed + ".txt"
    if len(result) > 50:
        max_base = 50 -4
        result = result[:max_base] + ".txt"
    return result

print(sanitize_filename("Ancient Scroll.txt"))
print(sanitize_filename("Quest 2042! (Epic)"))
print(sanitize_filename("notes"))
print(sanitize_filename("X" * 60))
print(sanitize_filename("test.pdf"))

# Alternative Method 2

def sanitize_filename(filename):
    clean = filename.lower().replace(" ", "_")
    safe = ""
    for char in clean:
        if char.isalnum() or char in ".-_":
            safe += char
    if not safe.endswith(".txt"):
        if "." in safe:
            safe = safe[:safe.rfind(".")]
        safe += ".txt"
    if len(safe) > 50:
        safe = safe[:46] + ".txt"
    return safe

print(sanitize_filename("Ancient Scroll.txt"))
print(sanitize_filename("Quest 2042! (Epic)"))
print(sanitize_filename("notes"))
print(sanitize_filename("X" * 60))
print(sanitize_filename("test.pdf"))