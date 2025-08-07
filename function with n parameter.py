#  passing multiple value in a function
# convert all those value in list
# perform action on list and find average of those number 

def fun1(*g):      # this *g will help you to receive argument as tuple
    print (g)
    print()  #  create a blank line 
    return g

x=fun1(1,2,3,4,5,6,6,8,9,9,8,75,45,35,36,6,6,3,7,79)   #  this will convert the formal arguments into tuple  
y=list(x)                                              # this will convert the tuple into list
print(y)                                               # now you can perform built-in function on this list

# to find the average of all those number in the list
total=0
for i in y:
    total=total+i
average = total/len(y)
print()
print("average of those numbers are :",average)

'''
               output 
(1, 2, 3, 4, 5, 6, 6, 8, 9, 9, 8, 75, 45, 35, 36, 6, 6, 3, 7, 79)

[1, 2, 3, 4, 5, 6, 6, 8, 9, 9, 8, 75, 45, 35, 36, 6, 6, 3, 7, 79]

average of those numbers are : 17.65

'''
