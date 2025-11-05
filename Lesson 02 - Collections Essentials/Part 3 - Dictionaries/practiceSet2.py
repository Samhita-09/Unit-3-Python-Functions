# Question 1 & 2 - Code Tracing

# Question 3

def calculate_engagement_rate(post):
    if post["views"] == 0:
        return 0
    engagement = post["likes"] + post["comments"] + post["shares"]
    rate = engagement / post["views"]
    final_rate = rate * 100
    return f"{final_rate:.2f}"

print(calculate_engagement_rate({"views": 1000, "likes": 50, "comments": 10, "shares": 5}))
print(calculate_engagement_rate({"views": 0, "likes": 50, "comments": 10, "shares": 5}))