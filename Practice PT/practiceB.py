def reverse_words(sentence):
	if not sentence:
		return ""
	sentence_list = sentence.split()
	reversed = sentence_list[::-1]
	new = " ".join(reversed)
	return new.strip()

print(reverse_words("sentence i made"))

def find_longest(words):
    if not words:
        return "", 0
    longest_word = ""
    length = 0
    for word in words:
        if len(word) > length:
            length = len(word)
            longest_word = word
        elif len(word) == length:
            pass
    return longest_word, length

print(find_longest(["cat", "elephant", "dog"]))
print(find_longest(["hi", "bye"]))
print(find_longest(["hi", "my", "cry", "lie"]))
print(find_longest([]))

# REMEMBER THIS ONE TO PRACTICE
def merge_dicts(dict1, dict2):
    new_dict = dict1
    new_dict.update(dict2) # remember this automatically replaces dict1's thing if they have the same key.
    return new_dict

print(merge_dicts({"a": 1}, {"b": 2}))
print(merge_dicts({"x": 10}, {"x": 20}))
print(merge_dicts({}, {"key": "value"}))

def grade_calculator(*scores, curve=0):
    try:
        avg = sum(scores) / len(scores) + curve
        if avg > 90:
            letter_grade = "A"
        elif avg < 90 and avg > 79:
            letter_grade = "B"
        elif avg < 80 and avg > 69:
            letter_grade = "C"
        elif avg < 70 and avg > 59:
            letter_grade = "D"
        else:
            letter_grade = "F"
        return avg, letter_grade
    except ZeroDivisionError:
        return (0, "F")
    
print(grade_calculator(85, 90, 80))
print(grade_calculator(70, 75, curve=10))
print(grade_calculator())