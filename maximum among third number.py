#this program is for finding maximum number among three number
x=int(input("enter first number:"))
y=int(input("enter second number :"))
z=int(input("enter third number :"))

if x>y and x>z:
    print(x,"is greater")
elif y>x and y>z:
    print(y,"is greater")
elif z>x and z>y:
    print(z,"is greater")



'''
enter first number:65463
enter second number :24525
enter third number :2314
65463 is greater
'''
