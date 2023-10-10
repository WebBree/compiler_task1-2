import re

def is_valid_identifier(identifier):
    # Regular expression pattern to match a valid identifier
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    
    # Use re.match() to check if the identifier matches the pattern
    if re.match(pattern, identifier):
        return True
    else:
        return False

# Input from the user
identifier = input("Enter an identifier: ")

# Check if the identifier is valid
if is_valid_identifier(identifier):
    print(f"'{identifier}' is a valid identifier.")
else:
    print(f"'{identifier}' is not a valid identifier.")
