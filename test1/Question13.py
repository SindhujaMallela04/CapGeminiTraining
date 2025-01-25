#function to get user input
def get_input():
    while 1:
        entered_string = input("Enter a string or a number to check for palindrome: ")
        if entered_string == "":
            print("You did not enter anything. Please try again.")
            print()
            continue        
        return entered_string
#function to check if the entered string is a palindrome
def check_palindrome(entered_string):
    if entered_string == entered_string[::-1]:
        return True
    return False
#function to display the result
def display(entered_string, is_palindrome):
    if is_palindrome:
        print(f"{entered_string} is a palindrome")
    else:
        print(f"{entered_string} is not a palindrome")
#main function
def main():
    while(1):
        entered_string = get_input()
        copy_of_string = entered_string
        entered_string = entered_string.lower()
        display(copy_of_string, check_palindrome(entered_string))
        print()
        ans = input("Would you like to try other strings or numbers? (Yes/No): ")
        if ans == "Yes":
            continue
        else:
            break
main()

