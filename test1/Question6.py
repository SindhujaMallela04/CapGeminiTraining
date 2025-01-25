#importing the math module
import math
#function to check if the number is prime or not
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True
#function to get the input from the user
def get_input():
    while(1):
        lower_bound = int(input("Enter a whole number: "))
        upper_bound = int(input("Enter a whole number: "))
        if lower_bound < 0:
            print(f"Enter only positive numbers!!")
        else:
            return lower_bound, upper_bound
#function to display the prime numbers between the lower bound and upper bound
def display(lower_bound, upper_bound):
    for i in range(lower_bound, upper_bound + 1):
        if(is_prime(i)):
            print(f"{i} is a prime number")
#main function
def main():
    lower_bound, upper_bound = get_input()
    display(lower_bound, upper_bound)
main()
    