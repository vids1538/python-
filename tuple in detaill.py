#   this program is for tuple
'''  Tuple is a collection of element that can hold items of diffrent data types
   - ordered
   -unchangable ,once created tuple then you can't change the value
   but if you want to change then convert the tuple into list using
   list() constructor then you can change the data and after changing the data
    convert back using tuple constructor..

  -allow duplicates
  -slower than list
  -consume more memory than list l

  you can put data directly like

  y= 4,66,22,66,True,"rohan"
        or
  h=(1,2,3,44,22,77,22,33,5254,564,89)   - you can use small braces

  '''
h=(1,2,3,44,22,77,22,33,5254,564,89)
# if you want to sort this list then first you have to convert the tuple into list
#then perform action
m=list(h)
m[0]=42
m[1]=85
m.sort()
h=tuple(m)
print(h)# (3, 22, 22, 33, 42, 44, 77, 85, 89, 564, 5254)
