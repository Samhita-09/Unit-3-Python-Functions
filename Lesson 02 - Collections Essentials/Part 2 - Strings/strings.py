# announcement = " BERGEN TECH robotics meeting TODAY! "

def format_course_code(code):
    trimmed = code.strip()
    upper = trimmed.upper()
    return upper

print(format_course_code(" webdev101 "))
print(format_course_code(" Python202 "))
print(format_course_code("Java303"))

def count_hashtags(post):
    words = post.split(" ")
    count = 0
    for word in words:
        if word.startswith("#"):
            count += 1
    return count

post1 = "Great game today! #BergenTech #GoGamrz #Pride"
post2 = "Meeting tomorrow in room 205"
post3 = "#Robotics team wins #StateCampionship! #Stem #BergenTech"

print(f"There are {count_hashtags(post1)} hashtags in post1.")
print(f"There are {count_hashtags(post2)} hashtags in post2.")
print(f"There are {count_hashtags(post3)} hashtags in post3.")

filename = "assignment.pdf"
print(filename.endswith(".pdf")) # True
print(filename.endswith(".docx")) # False