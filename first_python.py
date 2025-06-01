#Write a Python program that asks the user for the following information:
 #   Name, Age, GPA (0-5, can be decimals), Field of Interest, Graduated ("yes" or "no").
#1- Print a nicely formatted 
#2- Based on the info, determine and print:
#If the user is eligible for a scholarship (age < 25, GPA ≥ 3.5, has graduated)
#If the user is eligible for an internship (age < 30, GPA ≥ 2.5)
#If neither, recommend they apply again later.

name = input("Enter your name:").capitalize()
age = int(input("Enter your age:" ))
gpa = float(input("whats your GPA:"))
field = input("What is your field of interest?").capitalize()
graduated_input = input("Have you graduated? (yes/no): ")

if graduated_input.lower() == "yes":
    graduated = True
else:
    graduated = False
print("Hello, this is " + name + ", I am " + str(age) + " years old. " + " My GPA is " +str(gpa) + ", im interested in " +field)


if  graduated  :

  print(" Yes I have graduateddd :) ")  
else: print(" Not yet graduated :(")

if age < 25 and gpa >= 3.5 and graduated == True:
    print("Congratulations " + name + "! You are eligible for a scholarship")
elif age < 30 and gpa >= 2.5:
    print("Congrats " + name + "! You are eligible for an internship")
else:
    print("Sorry " + name + "! You can apply later")

