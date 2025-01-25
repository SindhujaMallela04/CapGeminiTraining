#function to get user input
def get_input():
    num = int(input("Enter the number for calculating the factorial: "))
    if num < 0 :
        print("Enter positive numbers only!!")
    return num
#function to calculate the factorial
def calculate_factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    return fact
#function to display the factorial
def display(num, fact):
    print(f"Factorial of {num} is {fact}")
#main function
def main():
    num = get_input()
    fact =  calculate_factorial(num)
    display(num, fact)
main()
