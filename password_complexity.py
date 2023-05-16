def check_password_complexity(password):
    complexity = 0

    # Check length
    if len(password) >= 8:
        complexity += 1

    # Check for uppercase letters
    if any(char.isupper() for char in password):
        complexity += 1

    # Check for lowercase letters
    if any(char.islower() for char in password):
        complexity += 1

    # Check for numbers
    if any(char.isdigit() for char in password):
        complexity += 1

    # Check for special characters
    special_chars = "!@#$%^&*()-_=+[{]}\|;:'\",<.>/?"
    if any(char in special_chars for char in password):
        complexity += 1

    return complexity


def get_password_complexity_message(complexity):
    if complexity == 0:
        return "Very Weak: Your password does not meet any complexity criteria."
    elif complexity == 1:
        return "Weak: Your password meets the minimum complexity requirement."
    elif complexity == 2:
        return "Moderate: Your password has moderate complexity."
    elif complexity == 3:
        return "Strong: Your password has a strong level of complexity."
    elif complexity == 4:
        return "Very Strong: Your password has a very strong level of complexity."
    else:
        return "Invalid Complexity Level"


# Example usage
password = input("Enter a password: ")
password_complexity = check_password_complexity(password)

password_message = get_password_complexity_message(password_complexity)
print("Password Complexity:", password_message)
