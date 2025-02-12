

#  zip function  :

# Python's zip() function is a built-in function that is used to combine two or more iterables into a single iterable.

# The zip() function in Python is used to combine multiple lists, tuples, or strings into a single iterable of tuples.

# Why use zip()?

"""
1> Simplifies code: zip() can make code more efficient and easier to read 
2> Pairs data together: zip() pairs up elements from each iterable, creating tuples of corresponding elements 
3> Useful for loops: zip() can be especially useful in loops 
4> Transposes data: zip() can transpose a matrix, converting rows into columns 

"""
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)

# use the tuple() function to display a readable version of the result:

print(set(x))

# program 3

a=[1,2,3,4,5]

b=['a','b','c','d']

c={5,6,7,8,9}

print(zip(a,b))  # zip function is used to datatype 
# output : zip object at 0x73971630ff00>

print(list(zip(a,b))) #[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
print(tuple(zip(a,b)))# ((1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'))

print(set(zip(a,b))) # {(4, 'd'), (1, 'a'), (2, 'b'), (3, 'c')}
print(dict(zip(a,b))) # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
print(dict(zip(b,c))) #{'a': 5, 'b': 6, 'c': 7, 'd': 8}

# program : 4

a=[1,2,3,4,5]

b=['a','b','c','d']

for i in zip(a,b):
    print(i)
"""
output :

(1, 'a')
(2, 'b')
(3, 'c')
(4, 'd')
"""

# program :4 

a=[]
for i in zip(a,b):
    a.update(i)
print(a)

""""
a=[]
for i in range(1,15):
   print(a.update(i))
"""

# program :5

a={'a':1,'b':2,'c':3}
b=[1,2,3]
print(tuple(zip(a,b)))
print(tuple(zip(b,a)))

#output:
"""
(('a', 1), ('b', 2), ('c', 3))
((1, 'a'), (2, 'b'), (3, 'c'))
"""

