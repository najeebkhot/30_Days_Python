# Program to take input from the user and printing it as output

print("\nHello please enter yout information\n")

title = input("\nPlease enter your title (Mr./Ms.) : ")
first_name = input("\nPlease enter your first name : ")
last_name = input("\nPlease enter your last name : ")
age = int(input("\nPlease enter your age : "))
address = input("\nPlease enter your address in the format as city/country : ")
skills = input("\nPlease enter your skills separated by comma : ")
user_skills = skills.split(',')

print(f"\nHello {title} {first_name}  {last_name} please find below your personal information.")
print("\nPersonal Information")
print(f"\nName : {title} {first_name}  {last_name} \nAge : {age} \nAddress : {address} \nSkills : {user_skills}") 
print("\n\nThank You!!!")
