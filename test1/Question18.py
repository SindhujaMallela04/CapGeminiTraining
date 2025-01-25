#function to get user input
def get_input():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    return weight, height
#function to calculate BMI
def calculate_bmi(weight, height):
    return weight / (height ** 2)
#function to display the BMI
def display(bmi):
    print(f"Your BMI is {bmi:.2f}")
    if bmi < 18.5:
        print("Category : Underweight")
    elif 18.5 <= bmi < 25:
        print("Category: Normal")
    elif 25 <= bmi < 30:
        print("Category: Overweight")
    else:
        print("Category: obese")
#main function
def main():
    weight, height = get_input()
    bmi = calculate_bmi(weight, height)
    display(bmi)
main()