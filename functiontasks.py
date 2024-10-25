#Task1:
# def Python_function():
#     print("Hello,Guys!")

# Python_function()

#Task2:
# def add_numbers(num1 ,num2):
#     result = num1 + num2
#     print("the sum of two numbers is: ", result)

# add_numbers(20,30)

#Task3:
# import math
# def circle(radius_circle):
#     area = math.pi * (radius_circle**2)
#     return area

# radius_circle = float(input('Enter the radius of a circle:'))
# area = circle(radius_circle)
# print(f"the area of a circle with radius {radius_circle} is : {area} .")

#Task4:
# def two_numbers(a,b):
#     add = a + b
#     sub = a - b
#     product = a * b
#     return add,sub,product

# a = float(input('Enter a number:'))
# b = float(input('Enter b number:'))
# result = two_numbers(a,b)
# print(f"the sum of two numbers is:", result[0])
# print(f"the sub of two numbers is:", result[1] )
# print(f"the product of two numbers is:", result[2])

# Task5: Default parameter in Function:
# def power(base,exponent=2):
#     return base**2
# print("2 to raised power 2= ",power(2))
# print("3 to raised power 3= ",power(3,3))

# def greet(name="Guest"):
#     print("Hello,"+ name + "!")
# greet()
# greet("Alice")

# def sum_of_even(numbers):
#     total = 0
#     for num in numbers:
#         if num%2 == 0:
#             total+= num
#     return total
# num_list = [1,2,3,4,5,6]
# print("Sum of even number:",sum_of_even(num_list))

#ex1:
def farenheit_to_celcius(farenheit):
    celcius = (farenheit-32)*5/9
    return celcius
temp_in_f = 98.6
temp_in_c = farenheit_to_celcius(temp_in_f)
print(f"{temp_in_f}F is {temp_in_c:.2f}C")












