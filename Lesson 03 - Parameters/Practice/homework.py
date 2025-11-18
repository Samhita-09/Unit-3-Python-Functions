# Question 5

# Output1: 18.0
# Output2: 15.0

# Question 6

def make_notification(user, *messages, urgent=False):
    if urgent:
        urgent = "URGENT"
    elif urgent == False:
        urgent = "Not Urgent"
    return f"{urgent}: {user} - {messages}"

print(make_notification("admin", "Server down!", urgent=True))
print(make_notification("user", "Welcome", "Check inbox"))

# Question 7

# Output1: SELECT name, email FROM users LIMIT 10
# Output2: SELECT * FROM logs WHERE level='error' LIMIT 5

# Question 8

def log_action(actor, *actions, timestamp=None, **context):
    actionsStr = ""
    for action in actions:
        if actionsStr == "":
            actionsStr = action
        elif action not in actionsStr:
            actionsStr += ", " + action
    contextStr = ""
    for key, value in context.items():
        if contextStr == "":
            contextStr = f"{key}={value}"
        elif key not in contextStr:
            contextStr += ", " + f"{key}={value}"
    return f"{actor}: {actionsStr} | {contextStr}"

print(log_action("bot", "login", "scan", source="API", ip="1.2.3.4"))