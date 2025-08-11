#   function


def fun1(x,y,z,w):
    print(x+y+z+w)

fun1(11,33,111,556)

#  711   will be the output

fun1(12,13,w=14,z=24)   # 63

def fun2(*p):
    print(p)
    print(type(p))
    w=list(p)
    print(w)
    print(type(w))

fun2(11,22,44,55,66,33,66,77,43,667)

'''
(11, 22, 44, 55, 66, 33, 66, 77, 43, 667)
<class 'tuple'>
[11, 22, 44, 55, 66, 33, 66, 77, 43, 667]
<class 'list'>

you can also cconvert the tuple into list like this

'''
#variable length key keyword argument allow a function to accept unlimited no of argument
# in key :value pair

def vlka(**k):     # vlka:- variable length key keyword argument
    print(k,type(k))

vlka(aman=12,arush=42,bits=43,vids=91)
vlka(name="aman",id=21875,roll=40,mobile=7161905442)

'''
{'aman': 12, 'arush': 42, 'bits': 43, 'vids': 91} <class 'dict'>
{'name': 'aman', 'id': 21875, 'roll': 40, 'mobile': 7161905442} <class 'dict'>

'''
