# Instructions
# Implement password_strength(password). Return Weak if the password has fewer than 8 characters. 
# Return Medium if it has at least 8 characters but does not contain both letters and digits. 
# Return Strong if it has at least 8 characters and contains at least one letter and at least one digit. 
# Students may need to research isalpha and isdigit.


def password_strength(password):
    has_letters = any(char.isalpha() for char in password)
    has_digits = any(char.isdigit() for char in password)
    contains_both = has_letters and has_digits
    
    if len(password) < 8:
        return "Weak"
    elif len(password) >= 8 and not contains_both:
        return "Medium"
    else:
        return "Strong"
    
print(password_strength("password")) 
# Weak

