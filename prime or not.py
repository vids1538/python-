#prime number program
a=int(input("enter a number :"))
for i in range(2,a):
      if(a%i==0):
        print("not prime")
        break
else:
    print("prime")
