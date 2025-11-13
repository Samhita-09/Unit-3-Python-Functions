# Using keyword arguments
def create_gamer(username, level, xp, rank, online):
    """Create a gamer profile."""
    return {
        "username": username,
        "level": level,
        "xp": xp,
        "rank": rank,
        "online": online
    }
    
player1 = create_gamer(
    username="BTStudent", 
    level=25,
    rank="gold",
    xp=10000,
    online=True
    )

print(player1)

# Practice

def send_message(sender, recipient, message, urgent):
    return f"{sender} --> {recipient}: {message} (Urgent: {urgent})"

message = send_message(
    sender="Alex",
    recipient="Jordan",
    message="Check Discord",
    urgent=True
)

print(message)

# Practice
def post_content(username, text, likes=0, retweets=0):
    return f"@{username}: {text} | 💖 {likes} | 🔁 {retweets}"

content = post_content("techguru", "Python is amazing!")

print(content)

# *args - Accept any number of values

def sum_scores(*scores):
    """Sum any number of scores"""
    total = 0
    for score in scores:
        total += score
    return total

print(sum_scores(2, 4, 6 , 8, 10))