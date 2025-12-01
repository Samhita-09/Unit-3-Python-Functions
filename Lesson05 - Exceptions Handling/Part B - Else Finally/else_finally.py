# Else - everything worked! Runs ONLY if the try block succeeded (no exceptions).
try:
    # Try something risky
    score = int(input("Enter score: "))
except ValueError:
    # Runs if it FAILED
    print("Invalid score!")
else:
    # Runs if it SUCCEEDED
    print(f"✅Score recorder: {score}")
    

def parse_command(message):
    """Parse a Discord command like: !ban PlayerName 7days"""
    try:
        parts = message.split()
        command = parts[0]
        target = parts[1]
        duration = parts[2]
    except IndexError:
        print("❌Invalid command format - missing parts!")
        return None
    else:
        print("✅Command parsed successfully!")
        if command.startswith("!"):
            print(f"⚡Executing: {command}")
        return command, target, duration
    finally: # Runs no matter what
        print("This block runs regardless of everything else!")
    
print(parse_command("!ban PlayerName 7days"))
print(parse_command("!ban"))