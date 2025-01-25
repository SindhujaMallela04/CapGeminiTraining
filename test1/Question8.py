#function for getting input from user
def get_input():
    num = int(input("Enter a number to get the Multiplication Table: "))
    num_range = int(input("Enter the range of the table: "))
    return num, num_range
#function to calculate and display the multiplication table
def calculate_and_display(num, num_range):
    print()
    print(f"Multiplication table of {num} : ")
    for i in range (1, num_range + 1):
        res = num * i
        print(f"{num} x {i} = {res}")
#main function
def main():
    num, num_range = get_input()
    calculate_and_display(num, num_range)
main()