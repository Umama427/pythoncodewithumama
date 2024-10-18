l = [11,45,1,2,4,6,1,1]
print(l)
# l.append(7)
# print(l)
# l.sort() #-> ascending order
# l.sort(reverse=True) #-> descending order
# l.reverse()# -> orignial list ko reverse krdeta hai 
# print(l.index(1)) #-> 1 jo hai index 2 pr hai return 2 de dy gh
print(l.count(1)) # -> agr main count krna cha houn 1 kitni br a rha hai
# m = l.copy() #-> m list ko l list ko copy krdeta hai
# m[0] = 0
# l.insert(1,899) #-> 1 index pr 899 insert krdega
m = [900,1000,1100]
# k = l + m#-> l and m ko concatenate krdega
# print(k)
l.extend(m) #-> l list me m list ko extend krdega
print(l)