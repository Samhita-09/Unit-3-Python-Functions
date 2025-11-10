# Question 1 - Tracing
# Ouput: 2300
# peak is the first item in viewers: 1240, and i starts out as 1. While i is less than the length of the list, look through it to see if viewers[i] is greater than peak. If it is, peak becomes that number and 1 gets added to i to continue the loop.

# Question 2 - Tracing
# Ouput: "WOW WOW LFG"
# Words splits the message at each space, creating a list with each individual word. Then filtered is set to equal an empty string, and the words list is iterated through with a for...in loop. If the length of the word is less than or equal to 5, the word gets added to the empty string, filtered, and a space is added after it. The final result prints the filtered string after removing any leading or trailing zeros.

# Question 3 - writing
def find_top_donor(donations):
    username = ""
    highest = 0
    for key, value in donations.items():
        if value > highest:
            highest = value
            username = key
    return username
    
            
        
    
donations = {
    "neon": 250,
    "vibe": 180,
    "lunar": 400,
    "pixel": 150
}

print(find_top_donor(donations))