# this program is for some inbuilt function

# bin ,oct,hex,max,min,len,id

x=int(input("enter a number:"))
y=bin(x)
print("binary of x is ",y)
print("octal of x is ",oct(x))
print("hexadecimal of x is ",hex(x))
print("address of x is ",id(x))

g=[11,22,33,44,55,34,2,4,32452,5,2,52,5,5,2,25,525]
print("minimum is ",min(g))
print("maximum is ",max(g))
print("length is ",len(g))
print("address of g is ",id(g))

'''              -:output:-

enter a number:77
binary of x is  0b1001101
octal of x is  0o115
hexadecimal of x is  0x4d
address of x is  140708932308264
minimum is  2
maximum is  32452
length is  17
address of g is  2160959232320
'''




