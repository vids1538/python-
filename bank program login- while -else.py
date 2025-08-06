#  bank program
password=1234
c=0
while (c!=3):
    c=c+1
    pin=int(input("enter your pin:"))
    if (pin==password):
        print("transaction successfull!")
        break
    else:
        print("incorrect pin")
else:
    print("card blocked!")


'''
if you enter wrong pin

enter your pin:2124
incorrect pin
enter your pin:1324
incorrect pin
enter your pin:4232
incorrect pin
card blocked!

if your pin is right

enter your pin:1245
incorrect pin
enter your pin:134
incorrect pin
enter your pin:1234
transaction successfull!

'''
