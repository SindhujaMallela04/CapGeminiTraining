#function to get user input
def get_input():
    Salary = float(input("Enter the salary: "))
    age = int(input("Enter the age: "))
    credit_score = int(input("Enter the credit score: "))
    return Salary, age, credit_score
#function to check eligibility for loan
def check_eligibility(Salary, age, credit_score):
    if Salary < 30000:
        print("Loan Rejected, Salary is less than 30000") 
    if age < 18:
        print("Loan Rejected, Age is less than 18")    
    if credit_score < 700:
        print("Loan Rejected, Credit score is less than 700")
    if Salary >= 30000 and age >= 18 and credit_score >= 700:
        print("Loan Approved")
        return
#main function
def main():
    Salary, age, credit_score = get_input()
    check_eligibility(Salary, age, credit_score)
main()
