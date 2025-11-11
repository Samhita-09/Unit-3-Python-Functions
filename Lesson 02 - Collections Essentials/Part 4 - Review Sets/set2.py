# Question 1 - Tracing
# 1300, 1500, 2700, 1500
# Output1: 4
# Output2: 7000

# Question 2 - Tracing
# Prints the first nine characters, then adds "..."
# Output: 0x9F1aB3c...

# Question 3 - Writing

def portfolio_value(holdings, prices):
    total = 0
    for key, value in holdings.items():
        multiplied = value * prices[key]
        total += multiplied
    return f"{total:.2f}"
    
holdings = {"BTC": 0.5, "ETH": 8.2, "SOL": 50}
prices = {"BTC": 62400, "ETH": 2480, "SOL": 142}

print(portfolio_value(holdings, prices))