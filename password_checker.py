# Simple Password Strength Checker
def check_password_strength(password):
    if len(password) < 6:
        return "Weak"
    elif len(password) < 10:
        return "Medium"
    else:
        return "Strong"

password = input("Enter your password: ")
strength = check_password_strength(password)
print(f"Your password is {strength}")

