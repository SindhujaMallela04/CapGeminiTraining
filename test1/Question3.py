#importing the random module
import random
#function to generate a random number between 1 and 100
def random_number_generation():
    return random.randrange(1, 101)
#function to guess the number
def guess():
    answer = random_number_generation()
    while (1):
        num = int(input("Enter a number between 1 and 100"))
        if num<0 or num>100:
            num = int(input("Enter a number between 1 and 100"))
        if num < answer:
            print(f"{num} is too low, guess again.")
        elif num > answer:
            print(f"{num} is too high, guess again")
        else:
            print("You are correct!!")
            return num
#main function
def main():
    print("Welcome to the Number Guessing Game")
    guess()
main()