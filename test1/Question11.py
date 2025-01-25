#function to get user input
def get_input():
    password = input("Enter the password: ")
    return password
#function to check the password
def check_password(password):
    if len(password) < 8:
        return False
    upper = False
    lower = False
    digit = False
    special = False
    for char in password:
        if char.isupper():
            upper = True
        if char.islower():
            lower = True
        if char.isdigit():
            digit = True
        if not char.isalnum():
            special = True
    if upper and lower and digit and special:
        return True
    return False

#main function
def main():
    password = get_input()
    while 1:
        if check_password(password):
            print("The password is valid")
            break
        else:
            print("Check the password requirements and try again")
            print("Requirements: ")
            print("1. At least 8 characters long")
            print("2. At least one uppercase letter")
            print("3. At least one lowercase letter")
            print("4. At least one digit")
            print("5. At least one special character")
            password = get_input()
main()
