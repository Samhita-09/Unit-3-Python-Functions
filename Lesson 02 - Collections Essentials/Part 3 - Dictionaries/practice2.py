# Question 1 - Code Tracing

# Output: {"key_a": "value1", "key_b": 150, "key_d": 50}
# Output2: False

# Question 2 - Code Tracing

# Output1: 120
# Output2: 60

# Question 3 - Code Writing

def get_user_bio(user):
    bio = user.get("bio")
    if not bio:
        return "No bio available"
    return bio

print(get_user_bio({"username": "coder", "bio": "Python enthusiast"}))
print(get_user_bio({"username": "newbie"}))

# Question 4 - Code Tracing

# Ouput1: 60
# Ouput2: 160

# Question 5 - Code Tracing

# Ouput1: 2

# Question 6 - Code Writing

def get_total_engagement(post):
    likes = post.get("likes")
    comments = post.get("comments")
    shares = post.get("shares")
    if not likes:
        likes = 0
    if not comments:
        comments = 0
    if not shares:
        shares = 0
    return likes + comments + shares

print(get_total_engagement({"likes": 100, "comments": 20, "shares": 10}))
print(get_total_engagement({"likes": 50, "comments": 5}))
print(get_total_engagement({"views": 1000}))

# Question 7 - Code Tracing

# Output1: 3
# Output2: 3

# Question 8 - Code Tracing

# Ouput1: {"key1": "value1", "key2": 200, "key3": 50}
# Ouput2: {"key1": "value1", "key2": 100, "key4": True}

# Question 9 - Code Writing

def find_most_followed(users):
    if not users:
        return None
    most_followers = 0
    for user in users:
        if user["followers"] > most_followers:
            most_followers = user["followers"]
            user_most_followed = user["username"]
    return user_most_followed

users = [
    {"username": "alex", "followers": 1000},
    {"username": "sam", "followers": 5000},
    {"username": "jordan", "followers": 3000}
]

print(find_most_followed(users))