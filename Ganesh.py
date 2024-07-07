def check_password_strength(password: str) -> bool:
    # Check length
    if len(password) < 8:
        return False
    
    # Check for at least one uppercase letter
    has_upper = any(c.isupper() for c in password)
    if not has_upper:
        return False
    
    # Check for at least one lowercase letter
    has_lower = any(c.islower() for c in password)
    if not has_lower:
        return False
    
    # Check for at least one digit
    has_digit = any(c.isdigit() for c in password)
    if not has_digit:
        return False
    
    # Check for at least one special character
    special_characters = "!@#$%^&*"
    has_special = any(c in special_characters for c in password)
    if not has_special:
        return False
    
    # If all criteria are met
    return True

# Take password input from user
password = input()

# Check password strength
if check_password_strength(password):
    print("True")
else:
    print("False")
