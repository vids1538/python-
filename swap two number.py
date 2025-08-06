# write a program for swap two number using third variable and without third variable

x=int(input("enter first number :"))
y=int(input("enter second number :"))

temp=x
x=y
y=temp
print("after swapping the value of first number is ",x)
print("after swapping the value of second number is ",y)
print(end='\n\n\n\n')

print("swapping without using third variable")
m=int(input("enter first number :"))
n=int(input("enter second number :"))
m=m+n
n=m-n
m=m-n

print("after swap first number =",m)
print("after swap second number =",n)

'''
enter first number :55
enter second number :33
after swapping the value of first number is  33
after swapping the value of second number is  55




swapping without using third variable
enter first number :67
enter second number :33
after swap first number = 33
after swap second number = 67

'''
