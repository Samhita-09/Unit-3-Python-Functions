# Question 1 - User Search with Tricky Trio

def search_user_database(searchquery):
    if not searchquery or searchquery == " ":
        return None, "No search query", False
    for char in searchquery:
        if not (char.isalpha() or char.isspace()):
            return False, "Invalid characters", False
    users = ["alice", "bob", "john", "johnny"] # i didn't know what database we were supposed to search, so I just made something up
    stripped = searchquery.lower().strip()
    count = 0
    for user in users:
        if stripped in user:
            count += 1
            result = count
            message = f"Found {result} user(s) matching '{searchquery}"
            success = True

    if count == 0:
        return 0, "No users found", True
    
    return result, message, success

# TEST 1: Empty string → None (no value provided)
result, message, success = search_user_database("")
print(result) # None
print(message) # "No search query"
print(success) # False

# TEST 2: Whitespace only → None (no value provided)
result, message, success = search_user_database(" ")
print(result) # None
print(message) # "No search query"
print(success) # False

# TEST 3: Has numbers → False (operation failed)
result, message, success = search_user_database("user123")
print(result) # False
print(message) # "Invalid characters"
print(success) # False

# TEST 4: Has special chars → False (operation failed)
result, message, success = search_user_database("user@email")
print(result) # False
print(message) # "Invalid characters"
print(success) # False

# TEST 5: Valid but no results → 0 (valid count of zero)
result, message, success = search_user_database("admin")
print(result) # 0
print(message) # "No users found"
print(success) # True ← Search worked! Just found nothing

# TEST 6: Valid with results → positive int
result, message, success = search_user_database("john")
print(result) # 2
print(message) # "Found 2 users"
print(success) # True

    
# Question 2 - Book Collection Stats
def analyze_book_pages(books):
    if not books:
        return 0, 0, 0.0, False
    total_items = len(books)
    total_pages = sum(books)
    avg = total_pages / total_items
    long = False
    for book in books:
        if book > 500:
            long = True
    return total_items, total_pages, avg, long

# TEST 1: Mixed collection with one long book
total_items, total_pages, avg, long = analyze_book_pages([250, 180, 620, 310])
print(total_items) # 4
print(total_pages) # 1360
print(avg) # 340.0
print(long) # True

# TEST 2: No long books
total_items, total_pages, avg, long = analyze_book_pages([200, 150, 300])
print(total_items) # 3
print(total_pages) # 650
print(avg) # 216.67 (approximately)
print(long) # False (all books ≤ 500)

# TEST 3: Empty list - EDGE CASE!
total_items, total_pages, avg, long = analyze_book_pages([])
print(total_items) # 0
print(total_pages) # 0
print(avg) # 0.0
print(long) # False

# TEST 4: Exactly 500 pages - TRICKY!
total_items, total_pages, avg, long = analyze_book_pages([500, 400, 300])
print(long) # False (500 is NOT > 500)

# TEST 5: Exactly 501 pages
total_items, total_pages, avg, long = analyze_book_pages([501, 400, 300])
print(long) # True (501 IS > 500)