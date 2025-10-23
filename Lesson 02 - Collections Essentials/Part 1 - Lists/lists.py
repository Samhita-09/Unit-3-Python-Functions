'''
            JS        vs          Python
create:  [1, 2, 3]              [1, 2, 3]
add:     .push(val)            .append(val)
remove:   .pop(val)             .pop(val)
'''

# Creating lists
daily_likes = [500, 600, 750, 400]
usernames = ["@nasa", "@tswift", "@netflix"]
mixed_data = [500, "likes", "@user123", True]
# Acessing elements
first_day = daily_likes[0] # 500
last_day = daily_likes[-1] # 400
third_day = daily_likes[2] # 750
# Slicing (like JS slice())
first_three = daily_likes[0:3] # [500, 600, 750]
last_two = daily_likes[-2:] # [400, 750]

# Information

length = len(daily_likes) # 4
maximum = max(daily_likes) # 750
minimum = min(daily_likes) # 400
sum = sum(daily_likes) # 2250

# Code along - post analyzer
def analyze_post(likes_list):
    if likes_list:
        total = sum(likes_list)
        average = total/(len(likes_list))
        best_day = max(likes_list)
        return (average, best_day)
    return "enter valid values"
    
# Practice question 1

def format_usernames(handles):
    if handles:
        formatted_handles = []
        for username in handles:
            formatted_handles.append("@" + username)
        return formatted_handles
    return "enter a valid username"

print(format_usernames(["nasa", "tswift", "netflix"]))

# Practice question 2

def  filter_trending_posts(likes_list):
    trending_posts = []
    for post in likes_list:
        if post > 1000:
            trending_posts.append(post)
    return trending_posts

print(filter_trending_posts([500, 1200, 800, 1500, 600]))

# Code tracing 1

