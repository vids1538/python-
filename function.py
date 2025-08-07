#this is the program for function
'''
function has 4 types
1. takes nothing return nothing
2. takes something return nothing
3. takes nothing return something
4. takes something return something 

'''

def first():       # function difination 
    print("hello this is first function!")

def add(m,n):      # formal parameter
    o=m+n
    print("addition is :",o)

def sub(a,b):
    c=a-b
    return c
def mul(m,n):
    print("multiplication is :",m*n)

first()
z=int(input("enter first number :"))
y=int(input("enter second numbe :"))
add(z,y)    # actual parameter
subtract =sub(z,y) 
print("subtraction is :",subtract)
m=mul(z,y)
print("multiplication is:",m)   #  multiplication is: None  print krega because 
                                #mul function is not returning anything




'''
hello this is first function!
enter first number :23
enter second numbe :66
addition is : 89
subtraction is : -43
multiplication is : 1518
multiplication is: None
'''
