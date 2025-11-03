# Question 2 - Write a function to find all players above a certain score.

def find_top_players(players, min_score):
    players_above_min = []
    for player in players:
        if player["score"] >= min_score:
            players_above_min.append(player["username"])
    return players_above_min

players = [
    {"username": "Dragonslayer", "score": 8500},
    {"username": "NinjaWarrior", "score": 6200},
    {"username": "MageKing", "score": 9100},
    {"username": "ShadowAssassin", "score": 5800}
]

result = find_top_players(players, 7000)
print(result)

# Question 3 - Code Tracing

# Output1: 9
# Output2: "EYE OF THE TIGER"
# Output3: "BLINDING LIGHTS"

# General Explanation: The playlists variable is a dictionary in which each value is a list. A variable, all_songs, is assigned an empty list. A for loop is then used to iterate through the playlist_name key in the dictionary and the value for each of those keys. Then, another for loop inside that one is used to go through each value list and get the individual strings inside those, converting them to uppercase and adding them to the all_songs list.
# Output1 Explanation: The first print statement asks for the length of the all_songs string, which consists of nine strings, so the length is nine.
# Output2 Explanation: The second print statement asks for index zero of all_songs, which is just the first item in it, which is "Eye of the Tiger". All the strings have been converted to uppercase letters, so it prints "EYE OF THE TIGER".
# Output3 Explanation: The third print statement asks for index negative one of all_songs, which is the last item in it, which is "Blinding Lights". All the strings have been converted to uppercase letters, so it prints "BLINDING LIGHTS".

# Question 4 - Calculate the total cost of items in a shopping cart

def calculate_cart_total(cart):
    total = 0
    for item in cart:
        total += item["price"] * item["quantity"]
    return total

cart = [
    {"item": "Laptop", "price": 899.99, "quantity": 1},
    {"item": "Mouse", "price": 24.99, "quantity": 2},
    {"item": "Keyboard", "price": 79.99, "quantity": 1},
    {"item": "USB Cable", "price": 9.99, "quantity": 3}
]

total = calculate_cart_total(cart)
print(f"Total: ${total:.2f}")