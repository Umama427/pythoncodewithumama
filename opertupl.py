# convert tuple into list then changes then again list into tuple
# countries = ("Spain", "Italy", "India", "England", "Germany")
# temp = list(countries)
# temp.append('Russia')       #add item
# temp.pop(3)                 #remove item
# temp[2] = "Finland"         #change item
# countries = tuple(temp)
# print(countries)

# concatenate two tuples into one
# countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
# countries2 = ("Vietnam", "India", "China")
# southEastAsia = countries + countries2
# print(southEastAsia)

# count method
tuple1 = (0, 1, 2, 3, 2, 31, 1,3,2,3)
res = tuple1.count(3)
res = tuple1.index(3)
res = tuple1.index(3,4,8) #slicing 4,8,then 3 is the value of index
res = len(tuple1)
print('Count of 3 in tuple1 is:', res)


