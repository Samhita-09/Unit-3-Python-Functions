# Question 1 - Tracing
# current = 3
# current = 0
# current = 5
# current = 7
# current = 15
# current = 16
# current = 23
# Output: [23]

# Question 2 - Tracing
# It starts at i = 1, so it starts at N. After the s, there's a bracket, so it stops.
# Ouput: NEXUS

# Question 3 - Writing
def match_mvp(players):
    mvp = ""
    best_kd_ratio = 0
    for key, value in players.items():
        kd_ratio = value["kills"] / value["deaths"]
        if kd_ratio > best_kd_ratio:
            best_kd_ratio = kd_ratio
            mvp = key
    return mvp
        

players = {
    "phoenix": {"kills": 28, "deaths": 12},
    "cipher": {"kills": 35, "deaths": 15},
    "blaze": {"kills": 22, "deaths": 18}
}

print(match_mvp(players))