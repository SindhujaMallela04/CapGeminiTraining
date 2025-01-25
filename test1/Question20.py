#function to print numbers from 1 to 100, but for multiples of 3 print "Fizz" instead of the number 
# and for the multiples of 5 print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz".
def display():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
#main function
def main():
    print("Program to print numbers from 1 to 100")
    display()
main()