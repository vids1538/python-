''' in this program we use seprator in print () function
print function has built-in  memory named sep which has blank space that's why
it give white space after using ,
'''
print("enter first number:")
x=input()
print("hello world")
print("enter second number ")
y=input()
print(x,y)

print(x,y,sep='k')



x=input("enter first number :")
y=input("enter second number :")
print(x,y,sep='*')
print()
print() # this will help you to change the line and also print something
print(end='           ')  #  this will now not change the line this will give you space  whatever space you defined
print("end")
print(end='\n\n\n\n')   # this will change 4 line
print("end here ")

'''
enter first number:
55
hello world
enter second number 
44
55 44
55k44
enter first number :66
enter second number :88
66*88


           end




end here 

'''
