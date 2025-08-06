# list just like arrray in other language
# list can also store hetrogenous data like this 

h=[11,22,33,44.54,'aman',"abhishek",44+5j]
for i in h:
    print(i)

'''
11
22
33
44.54
aman
abhishek
(44+5j)   # this is the complex number 
'''

g1=h=[11,22,33,44,45,77]
g1.append(49)  # this will append means add 49 at last index

#g1.clear()  this function will clear the list but not delete it

# del g1    # this will delete the g1 memory

g1.sort()  # ascending order only

print(g1)  #[11, 22, 33, 44, 45, 49, 77]

m=g1.reverse()  # descending order now

print(g1)  # [77, 49, 45, 44, 33, 22, 11]

g1.remove(44)
print(g1)  # [77, 49, 45, 33, 22, 11]

g1.pop(1)
print(g1)  #[77, 45, 33, 22, 11]

g1.insert(1,49)
print(g1)   #[77, 49, 45, 33, 22, 11]



