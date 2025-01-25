#function to get user input
def get_input():
    total_bill_amount = float(input("Enter the Total Bill Amount: "))
    number_of_people =  int(input("Enter the number of people: "))
    ans = input("Is there a tip percentage? (Yes/No) : ")
    if ans == "Yes":
        tip_percentage = int(input("Enter the tip percentage in number: "))
        return total_bill_amount, number_of_people, tip_percentage
    elif ans == "No":
        return total_bill_amount, number_of_people, 0
#function to calculate the amount per person    
def calculate(total_bill_amount, number_of_people, tip_percentage):
    tip = total_bill_amount * (tip_percentage/100)
    total_amount = total_bill_amount + tip
    amount_per_person = total_amount / number_of_people
    return amount_per_person
#function to display the amount per person
def display(amount_per_person):
    print(f"Amount per person is: {amount_per_person}")
#main function
def main():
    total_bill_amount, number_of_people, tip_percentage = get_input()
    amount_per_person = calculate(total_bill_amount, number_of_people, tip_percentage)
    display(amount_per_person)
main()

    

