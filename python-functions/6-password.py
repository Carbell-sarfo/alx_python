def validate_password(password):
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        return False

    # Check if the password contains at least one uppercase letter, one lowercase letter, and one digit
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True

    if not (has_uppercase and has_lowercase and has_digit):
        return False

    # Check if the password contains spaces
    if ' ' in password:
        return False

    return True
Explanation:

The validate_password function takes a password password as input.
It checks if the password is at least 8 characters long using the len() function.
It uses a loop to check if the password contains at least one uppercase letter, one lowercase letter, and one digit using the isupper(), islower(), and isdigit() string methods, respectively.
If the password doesn't meet any of the criteria, the function returns False; otherwise, it returns True.
You can use this function to validate a password like this:

python
Copy code
result = validate_password("Password123")
print(result)  # Output: True

result = validate_password("weak")
print(result)  # Output: False
The function will return True if the password passes all the checks and False otherwise.





