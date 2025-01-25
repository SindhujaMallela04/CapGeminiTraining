#function to get input from user
def get_input():
    list_of_numbers = []
    num = 0
    print("Enter a list of numbers. Press Enter twice to stop.")
    while 1:        
        num = input("Enter a list of numbers: ")  
        if num == "":
            return list_of_numbers      
        list_of_numbers.append(int(num))        
#function to display the second largest number in the list
def display_second_largest_in_list(list_of_numbers):
    if len(list_of_numbers) == 0:
        print("The list is empty")
        return
    if len(list_of_numbers) == 1:
        print(f"The only number in the list is {list_of_numbers[0]}")
    list_of_numbers.sort()
    for i in range(len(list_of_numbers)-1, 0, -1):
        if list_of_numbers[i] != list_of_numbers[i-1]:
            print(f"The second largest number in the list is {list_of_numbers[i-1]}")
            return 
#function to display the entered list
def display_the_entered_list(list_of_numbers):
    print()
    print("The entered list is: ", list_of_numbers)
    print()
#main function
def main():
    list_of_numbers = get_input()
    display_the_entered_list(list_of_numbers)
    display_second_largest_in_list(list_of_numbers)
main()    
    

