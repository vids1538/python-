#   print dictionary using for loop
''' in this program i use for loop to print dictionary key and values pairs
'''

h1={44:"aman",66:"rohit","age":19,"weight":60}

for i in h1:
    print(i)
'''
only key printed 
44
66
age
weight
'''
for i in h1:
    print(h1[i])

'''
aman
rohit
19
60
'''
for i in h1:
    print(i,h1[i])
'''
44 aman
66 rohit
age 19
weight 60
'''
for i in h1:
    print(i,":",h1[i],sep='')

'''
44:aman
66:rohit
age:19
weight:60
'''
