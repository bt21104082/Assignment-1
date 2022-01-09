print("Assignment 1")
#QUESTION1
print("PYHTON PROGRAM TO FIND AVERAGE OF THREE GIVEN NUMBERS")

FIRST_No=float(input("Enter the FIRST number:- "))
SECOND_No=float(input("Enter the SECOND number:- "))
THIRD_No=float(input("Enter the THIRD number:- "))
AVERAGE=(FIRST_No + SECOND_No + THIRD_No) / 3

print("The Average of three given numbers is: " , AVERAGE)

print("")

#QUESTION 2
print("PYTHON PROGRAM TO CALCULATE THE INCOME TAX OF PERSON AFTER SEVERAL DEDUCTION OF MONEY (GROSS INCOME>$30000)")
gross_income=int(input("Please Enter the Gross Income:$ "))
numberofdependents=int(input("Please Enter the number of dependents: "))
#deduction1=Standard Deduction
deduction1=10000
#deduction2=Dependent Deduction
deduction2=int(3000*numberofdependents)
Taxable_income=int(gross_income)-int(deduction1)-int(deduction2)
Tax_rate=.20*Taxable_income
Tax=Taxable_income+Tax_rate
print("The total income tax of a person in $: " , Tax)


print("*****************")


#QUESTION 3
print("PYTHON PROGRAM TO STORE VALUES IN LISTS")
STUDENT=[]
SID=int(input("Enter the SID of the student= "))
Name=str(input("Enter the NAME of the student= "))
Gender=str(input("Enter the GENDER M(MALE),F(FEMALE),U(UNKNOWN) use capital letters = "))
Course_Name=str(input("Enter the COURSE NAME of the student= "))
CGPA=float(input("Enter the CGPA of the student= "))
STUDENT.append(SID)
STUDENT.append(Name)
STUDENT.append(Gender)
STUDENT.append(Course_Name)
STUDENT.append(CGPA)
print(STUDENT)


print("*****************")


#QUESTION 4
print("PYTHON PROGRAM TO ENTER THE MARKS OF FIVE STUDENTS")
list=[]
student_marks_1=int(input("Enter the Marks of First Student:"))
student_marks_2=int(input("Enter the Marks of Second Student: "))
student_marks_3=int(input("Enter the Marks of Third Student: "))
student_marks_4=int(input("Enter the Marks of Fourth Student: "))
student_marks_5=int(input("Enter the Marks of Fifth Student: "))
list.append(student_marks_1)
list.append(student_marks_2)
list.append(student_marks_3)
list.append(student_marks_4)
list.append(student_marks_5)
print("The Lists of marks of five students are as follows: " ,list)


print("*****************")


#QUESTION 5
print("PYTHON PROGRAM TO PRINT A SPECIFIED LIST IN A MANNER")
LIST=['Red','Green','White','Black','Pink','Yellow']
LIST.remove('Black')
print(LIST)
LIST[3]=('Purple')
print(LIST)


print("Professor name - Manish Sir")
print("By- Shourya Mishra")
print("SID-21104082")
print("Branch- Electrical")
