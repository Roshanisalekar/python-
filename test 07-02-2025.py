#1) Program :- 
a={}
print(type(a))
#output :- <class 'dict'>

#2) Program :- 
a=[]
print(a)
print(type(a))
#output :- []
#          <class 'list'>

#3) Program :- 
a=set()
print(a)
print(type(a))
#output :- set()
#          <class 'set'>

#4) Program :- 
a=list(tuple())
print(a)
print(type(a))
#output :- []
#          <class 'list'>

#5) Program :- 
a=(1,2,3,1,2,3,1)   
b=list(set(str(a)))
print(b)
print(type(b))
#output - ['1', '2', ')', ',', '(', ' ', '3']
#         <class 'list'>

#6) Program :- 
a=(1,2,3)   
b=[4,5,6]
#print(a+b)   #output :- TypeError: can only concatenate tuple (not "list") to tuple
print(a,b)    #output :- (1, 2, 3) [4, 5, 6]

#7) Program :- 
#c=a+b
#print(c)
#output :- TypeError: can only concatenate tuple (not "list") to tuple
d=a,b
print(d)
#output :- ((1, 2, 3), [4, 5, 6])

#8) Program :- 
#Indexing 
a=(1,2,3)
b=(4,5,6)
c=b[2],a[2],b[1],a[1]
print(c)
#output :- (6, 3, 5, 2)

#9) Program :- 
a=(1,2,3)
b=(4,5,6)
c=list(a[1: :1],b[0:1:1])
print(c)
#output :-  list expected at most 1 argument, got 2

#10) Program :- 
a=(1,2,3)
b=(4,5,6)
c=a[0],a[1],b[1],b[2]
print(set(c))
#output :- {1, 2, 5, 6} 

#11) Program :- 
a={'a':1,'b':2,'c':3}
print(a.values())
#output :- dict_values([1, 2, 3])

#12) Program :- 
a={'a':1,'b':2,'c':3}
print(a.values('c'))
#output :- TypeError: dict.values() takes no arguments (1 given)

#13) Program :- 
a={'a':1,'b':2,'c':3}
print(a.get('c'))
#output :-  3

#14) Program :- 
a={'a':1,'b':2,'c':3}
b=list(a.values())
print(b)
#output :- [1, 2, 3].

#15) Program :- 
a={'a':1,'b':2,'c':3}
c=set(a.items())
print(c)
print(type(c))
#output :- {('b', 2), ('c', 3), ('a', 1)}
#          <class 'set'>

#16) Program :- 
x={[(2,2)]}
print(x)
print(type(x))
#output :- TypeError: unhashable type: 'list'  #what is meant by  unhashable type

#17) Program :- 
for i in range(1,5):
    if i%2==0:
        print('1')
    else:
        print('0')
#output :- 0
#          1
#          0
#          1

#15) Program :-
for i in range(1,6):
    for j in range(1,5):
        if i%2==0:
            print('1')
        else:
            print('0')
    print()
#output :-      0
#               0
#               0
#               0

#               1
#               1
#               1
#               1

#               0
#               0
#               0
#               0

#               1
#               1
#               1
#               1

#               0
#               0
#               0
#               0

#19) Program :-
for i in range(1,6):
    for j in range(1,5):
        if i%2==0:
            print('1',end="*")
        else:
            print('0',end="*")
    print()
#output :- 0*0*0*0*
#          1*1*1*1*
#          0*0*0*0*
#          1*1*1*1*
#          0*0*0*0*