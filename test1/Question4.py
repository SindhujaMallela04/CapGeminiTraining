#Importing the math module
import math
#function to take input of the student's name and his marks in 5 subjects
def get_input():
    Student_Name = input("Enter the Student's name: ")
    sub1 = float(input("Enter the marks for maths: "))
    sub2 = float(input("Enter the marks for Science: "))
    sub3 = float(input("Enter the marks for Social: "))
    sub4 = float(input("Enter the marks for English: "))
    sub5 = float(input("Enter the marks for Hindi: "))
    return Student_Name, sub1, sub2, sub3, sub4, sub5

#function to calculate the total marks of the student
def Total_Marks(sub1, sub2, sub3, sub4, sub5):
    return sub1 + sub2 + sub3 + sub4 + sub5

#function to calculate the percentage of the student
def percentage(totalMarks):
    return (100/500) * totalMarks
#
def grade(percentage):
    if percentage >= 80 and percentage<=100:
        return "A"
    elif percentage >= 60 and percentage < 80:
        return "B"
    elif percentage >= 40 and percentage < 60:
        return "C"
    else:
        return "Fail"
#function to display the student's name, total marks, percentage and grade
def display(Student_Name, Total_Marks, percentage, grade):
    print(f"Student Name : {Student_Name}")
    print(f"Total Marks scored out of 500 : {Total_Marks}")
    print(f"Percentage Achieved out of 100 : {percentage}")
    print(f"Overall Grade Aquired : {grade}")
#main function
def main():
    Student_Name, sub1, sub2, sub3, sub4, sub5 = get_input()
    total = Total_Marks(sub1, sub2, sub3, sub4,sub5)
    percent = percentage(total)
    display(Student_Name, total, percent, grade(percent))
main()