# def average(a,b): # required argument
#   print("The average is", (a + b)/2)

# average(4,6)


def average(a,b,c=1): # default argument
  print("The average is", (a + b+c)/2)
# average(5,6)
#if i give to value in the average(1,5) so ignore the default value
# average(1,5)
# average(5) #if i want to give a value
# average(b=9)# if i want to give a value to b 
# average(b=9,a = 21) #keyword argument

# def name(fname, mname = "Jhon", lname = "Whatson"):
#       print("Hello,", fname, mname, lname)


# name("Amy","Agarwal","Jain")


# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)
# name(mname = "Peter", lname = "Wesker", fname = "Jade")


# as tuple
# def average(*numbers):
#   sum = 0
#   for i in numbers:
#     sum = sum + i
#   print("Average is: ", sum / len(numbers))
#   return sum / len(numbers) # wapis lejao c ka pas or print c krdo

# c = average(5,6,7,1)
# print(c)

#as a dictionary
def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")