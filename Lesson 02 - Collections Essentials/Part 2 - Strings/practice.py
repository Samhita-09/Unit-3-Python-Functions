# Question 3

def create_username(first_name, last_name):
    username = first_name + "_" + last_name
    lowercase = username.lower()
    return lowercase

# Alternative:

# def create_username(first_name, last_name):
#     return f"{first_name}_{last_name}".lower()

print(f"Username: {create_username("John", "Smith")}")
print(f"Username: {create_username("MARY", "Jones")}")
print(f"Username: {create_username("Alex", "TAYLOR")}")

# Question 6

def check_email(email):
    if "@" in email and email.lower().endswith(".com"):
        return True
    return False

# Alternative shorter way

# def check_email(email):
#     email_lower = email.lower()
#     return "@" in email_lower and email_lower.endswith(".com")
    
print(check_email("test@gmail.com"))
print(check_email("user@yahoo.COM"))
print(check_email("invalid.com"))
print(check_email("test@school.edu"))

# Question 9

def create_slug(title):
    return title.strip().lower().replace(" ", "-")

print(create_slug("My First Blog Post"))
print(create_slug(" Python Tutorial "))
print(create_slug("Web Development 101"))