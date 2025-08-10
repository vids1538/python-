#this program is to find all prime number in the range given by user
m=int(input("enter first value:"))
n=int(input("enter last value:"))

for x in range(m,n+1): 
    for i in range(2,x): 
        if(x%i==0):
            break
    else:
        if(x<2):
            continue
        else:
            print(x,end=' ')
            
