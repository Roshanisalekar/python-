
#FOR LOOP :- The for loop in Python is used to iterate over a sequence (like a list, tuple, or string) or other iterable objects. Iterating over a sequence means going through each element one by one. In this article, we're going to describe how to iterate over a python list, using the built-in function for.

# 1) Program :- 
for i in range(1,10):
    print(i)  
#output :- 1
#          2
#          3
#          4
#          5
#          6
#          7
#          8
#          9

# 2) Program :- 
for i in range(1,10):
    print(i,end=" ")
#output :- 1 2 3 4 5 6 7 8 9

# 3) Program :- 
for i in range(1,10):
    print(i,end=1)
#output :-  end must be None or a string, not int

# 4) Program :-
for i in range(11,16):
    print(i)
#output :- 11
#          12
#          13
#          14
#          15

# 5) Program :-
for i in range(11,16):
    print(i,end=" ")
#output :- 11,12,13,14,15

# 6) Program :-
for i in range(15,1,-3):
    print(i,end=" ")
#output :- 15 12 9 6 3 

# 7) Program :-
for i in range(1,15,-1):
    print(i,end=" ")
#output :- BLANK

# 8) Program :-
for i in range(25,1,-5):
    print(i)
#output :- 25
#          20
#          15
#          10
#          5

# 8) Program :-
a=5
for i in range(a,0,-1):
    print(i)
#output :- 5
#          4
#          3
#          2
#          1

# 9) Program :-   
a=5
for i in range(a,0,-2):
    print(i)
#output :- 5
#          3
#          1

# 10) Program :-
a=5
for i in range(a,0,-4):
    print(i)
#output :- 5
#          1

# 11) Program :-
a=5
for i in range(a,10,1):
    print(i-4)
#output :- 1
#          2
#          3
#          4
#          5
#or
# 11) Program :-
a=5
for i in range(1 a+1):
    print(i)
#output :- 1
#          2
#          3
#          4
#          5

# 12) Program :-
a=5
for i in range(13,a-1,-2):
    print(i,end=" ")
#output :- 13 11 9 7 5

# 13) Program :-
a=(1,2,3,4)
for i in range(a):
    print(i)

# 14) Program :-
a=(1,2,3,4)
for i in a:
    print(i)
#output :- 1
#          2
#          3
#          4

# 15) Program :-
a="mansi"
for i in a:
    print(i)
#output :- m
#          a
#          n
#          s
#          i

# 16) Program :-
a="mansi"
for i in range(a):
    print(i)
#output :- 'str' object cannot be interpreted as an integer

# 17) Program :-
a="mansi"
for i in range(len(a)):
    print(i)
#output :- 0
#          1
#          2
#          3
#          4

# 18) Program :-
a="mansi"
for i in range(len(a)+1,len(a)-4,-1):
    print(i)
#output :- 6
#          5
#          4
#          3
#          2
