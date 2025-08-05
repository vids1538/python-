#  this program is  of input function

x=input("enter first number :")
y=input ("enter second number :")
print(x+y)    # this will concatinate because of string type
              # input function always take input from keyboard as string.
              # so it will concatinate not add
a=int(x)
b=int(y)
print(a+b)  #  here is addition because before add we convert string type into int

print("after addition of those number ,result is :",a+b)


#or you can take input from user another way
m=int(input("enter first number :"))
n=int(input("enter second number :"))

o=float(input("enter first decimal number:"))
p=float(input("enter second decimal number "))

print("addition is ",m+n)
print("addition of float number is ",o+p)


'''
                              -:output:- 
enter first number :44
enter second number :55
4455
99
after addition of those number ,result is : 99
enter first number :66
enter second number :22
enter first decimal number:22.05
enter second decimal number 55.83
addition is  88
addition of float number is  77.88

'''
