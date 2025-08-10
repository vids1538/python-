
x=eval(input("enter a number:"))  # eval function
print(x,type(x))
'''
enter a number:3
3 <class 'int'>

enter a number:44.6
44.6 <class 'float'>

enter a number:34+15j
(34+15j) <class 'complex'>

'''

#if you want to take input in a single line

m,n=input("enter first number:"),int(input("enter second number"))    # single line input taking 
print(m,n)
print(type(n))
print(type(m))

'''
enter first number:22
enter second number44
22 44
<class 'int'>
<class 'str'>

'''

x,y,z=(input("enter three number by pressing spacebar not enter button ")).split(' ')  #  space se split hoga 
print(x,y,z)
print(type(x))

'''
enter three number:44 66 88
44 66 88
<class 'str'>

'''
x=input("enter date:(12/04/2005)").split('/')  # split function convert them into list 
print(x)

'''
enter date:12/08/2025
['12', '08', '2025']
'''

x=input("tell me about yourself").split()
print(x)
print(type(x))

'''
tell me about yourselfi am a student 
['i', 'am', 'a', 'student']
<class 'list'>
'''

x,y,z=[int(i) for i in input("enter 3 number:").split()]
print(x,y,z)
print(type(x))

'''
enter 3 number:11 44 77
11 44 77
<class 'int'>
'''
t1=list([eval(g) for g in input("enter data:").split()])
print(t1)
print(type(t1))
'''
enter data:22 44 55 66 212 55 667 892
[22, 44, 55, 66, 212, 55, 667, 892]
<class 'list'>
'''

d1=dict(input().split('-') for i in range(3))
print(d1,type(d1))

'''
12-"aam"
13-"anar"
14-"sev"
{'12': '"aam"', '13': '"anar"', '14': '"sev"'} <class 'dict'>

'''


