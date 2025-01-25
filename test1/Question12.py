#function to get user input
def get_input():
    num = int(input("Enter the length of the pattern: "))
    return num
#function to print the pattern
def pattern(num):
    for i in range (0, num):
        for j in range (0, i+1):
            print("*", end = "")
        print()
    
    ans = input("Print the pattern in reverse? Yes or No: ")
    if ans == "Yes":
        for i in range (num, -1, -1):
            for j in range (0, i):
                print("*", end = "")
            print()              
#main function
def main():
    num = get_input()
    pattern(num)
main()