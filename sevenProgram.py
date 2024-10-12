#day7:29 Sep 2024
#nested if statement and boolean logic

#1.
temp = 25
raining = False
if temp > 20 and not raining:
    print("Its a great day for a walk!.")
else:
    print("Maybe stay inside.")

#3.
person_age = int(input("Enter your age:"))
is_student = input("Are you a student (yes/no)?").lower()=="yes"
if person_age == 18:
    price = 5
elif is_student:
   price = 8
else:
    price = 10

print(f"Your ticket price is {price}$")