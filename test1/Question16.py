#function to get user input
def get_input():
    list_of_numbers = list(map(int, input("Enter the numbers separated by spaces: ").split()))
    return list_of_numbers
#function to split the list into even and odd numbers
def split_into_lists(list_of_numbers):
    list_of_even_numbers = []
    list_of_odd_numbers = []
    for number in list_of_numbers:
        if number % 2 == 0:
            list_of_even_numbers.append(number)
        else:
            list_of_odd_numbers.append(number)

    return list_of_even_numbers, list_of_odd_numbers
#function to display the even and odd numbers
def display(list_of_even_numbers, list_of_odd_numbers):
    print("List of Even Numbers: ")
    for even_number in list_of_even_numbers:
        print(even_number, end = " ")
    print()
    print("List of Odd Numbers: ")
    for odd_number in list_of_odd_numbers:
        print(odd_number, end = " ")
    print()
#main function
def main():
    list_of_numbers = get_input()
    list_of_even_numbers, list_of_odd_numbers = split_into_lists(list_of_numbers)
    display(list_of_even_numbers, list_of_odd_numbers)
main()
