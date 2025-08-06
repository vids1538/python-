#              slicing operator

#  [start:stop:step]

# suppose we have a list
h1=[6,4,6,7,8,54,3,534,543,6,36,534,5]
# we have to extract from 7 to 36
p=h1[3:11:1]
print(p)   #[7, 8, 54, 3, 534, 543, 6, 36]

print(h1[2::])    #[6, 7, 8, 54, 3, 534, 543, 6, 36, 534, 5]

print(h1[2::2])   #  [6, 8, 3, 543, 36, 5]


'''
 negative indexing means in this list [6, 8, 3, 543, 36, 5]
 5 has -1
 36 has -2
 543 has -3
 3 has -4
 8 has -5
 6 has -6 indexing
 '''
h2=h1.copy()
k=h2[-1]   # means h= [6,4,6,7,8,54,3,534,543,6,36,534,5]
print(k)  # 5


# means you can reverse the list using slicing operator like this 
p=h2[-1::-1]
print(p)   #  [5, 534, 36, 6, 543, 534, 3, 54, 8, 7, 6, 4, 6]

x="abhishek"
print(x[-1::-1])  # kehsihba


'''
here is the overall output
[7, 8, 54, 3, 534, 543, 6, 36]
[6, 7, 8, 54, 3, 534, 543, 6, 36, 534, 5]
[6, 8, 3, 543, 36, 5]
5
[5, 534, 36, 6, 543, 534, 3, 54, 8, 7, 6, 4, 6]
kehsihba
'''
