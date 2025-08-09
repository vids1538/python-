'''
*****
*****
*****
*****
*****
to print this pattern use this code..
'''
for i in range(1,6):
    for j in range(1,5):
        print("*",end='')
    print()

    

print(end='\n\n\n')

'''
*    
**   
***  
**** 
*****
'''

for i in range(1,6):
    for j in range(1,6):
        if( j<=i ):
            print("*",end='')
        else:
            print(" ",end='')
    print()



print(end='\n\n\n')


'''
*****
****
***
**
*
'''

for i in range(1,6):
    for j in range(1,6):
        if (j>=i):
            print("*",end='')
        else:
            print('',end='')
    print()

'''
*****
****
***
**
*
'''
print(sep='\n\n')

for i in range(1,6):
    for j in range(1,6):
        if (j<=6-i):
            print("*",end='')
        else:
            print('',end='')
    print()
'''
   *
  ***
 *****
*******
'''
for i in range(1,5):
    for j in range(1,8):
        if(j>=5-i and j<=3+i):
            print("*",end='')
        else:
            print('',end='')
    print()
