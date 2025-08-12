#  exception handling

x=int(input("enter first number:"))
y=int(input("enter second number:"))

try:
    z=x/y
    print("after division :",z)
except ZeroDivisionError:   #   this is a class of zero division error 
    print("why you dividing with zero")
except TypeError:     # this class is used when you devide a string with int 
    print("you can't devide a sting with number :")
print("thanks for using the program")
            
'''
you can also use exception class in a single except like this

try:
  z=x/y
  print(z)
  
except(ZeroDivisionError,TypeError):
     print("error")


And if you don't know the exception class name then

try:
   z=x/y
   print(z)

except:
    print("error")

'''
