#function to check if a year is a leap year or not
def Leap_Year_Checker(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
#function to get the input from the user and display the result
def get_input_and_display():
    while(1):
        year = int(input("Enter the year to check if it is a leap year or not: "))
        if year < 0:
            print(f"Enter only positive numbers!!")
        else:
            if(Leap_Year_Checker(year)):
                print(f"{year} is a leap year")
            else:
                print(f"{year} is not a leap year")
        continue_process = input("Do you want to check other years? (Yes/No): ")
        if continue_process == "No":
            break
#main function
def main():
    get_input_and_display()
main()