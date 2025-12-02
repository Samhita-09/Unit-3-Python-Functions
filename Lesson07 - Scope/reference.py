# SCOPE - the visibility of variables, where it can be seen and used (global or local).
# GLOBAL - outside all functions (visible everywhere)
# LOCAL - inside a function (only visible there)

# THE BUG
def add_bonus():
    score = score + 100 # python thinks its local

score = 500
add_bonus()