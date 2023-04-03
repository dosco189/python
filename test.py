#Get name from user 
input_name = input("Enter your name: ")

#Get birthday from user 
input_birthday = input("Enter your birthday (MM/DD/YYYY): ")

#Calculate age
a, b, c  = input_birthday.split("/")
age = 2023 - int(c)

#Print name and age
print("Hi", input_name, "you will be", age, "in 2023")