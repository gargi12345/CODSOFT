
print("Password must be of minimum 8 characters, should contain a special symbol (@, #, $), and a number.")
print("Example: abcdefg#1")

while True:
    password = input("Enter password: ")

    if len(password) < 8:
        print("Password is less than 8 characters")

    elif not any(char.isdigit() for char in password):
        print("Password does not contain a number")

    elif not any(char in '@#$' for char in password):
        print("Password does not contain a special symbol (@, #, $)")

    else:
        password1=input("Confirm password: ")

    if password==password1:
        print("Password generated successfully")
        break
    
    else:
        print("Passwords do not match")

    retry = input("Try again? (y/n): ")
    if retry.lower() != 'y':
        break
