
#While Loop :- A while loop in Python is a control flow statement that allows a block of code to be executed an indeterminatnumber #              of times, so long as the associated condition holds true.
#1) Program :- 
a=5
while a>1:
    print("*")
#Output :- infinity

#2) Program :- 
a=5
while a>1:
    print("*")
    a=a-1
#output :-  *
#           *
#           *
#           *

#3) Program :- 
a=5
while a>1:
    print("*",end=" ")
    a=a-1
#output :- * * * *

#4) Program :- 
a=5
#           ***
#           ** 

#5) Program :- 
a=5
while a>1:
    print((("*"*a)+" ")*a)
    a=a-1
#output :-  ***** ***** ***** ***** ***** 
#           **** **** **** **** 
#           *** *** *** 
#           ** **

#6) Program :- 
a=5
while a>=1:
    print((("*"*a)+" ")*a)
    a=a-1
#output :-  ***** ***** ***** ***** ***** 
#           **** **** **** **** 
#           *** *** *** 
#           ** **
#           *

#7) Program :- 
a = 0  
m = 65  
while a < 4:  
    for i in range(a + 1):  
        print(chr(m), end=" ")  
        m += 1 
    print()  
    a += 1
#output :-    A
#             B C
#             D E F
#             G H I J 

#Second way :- 
a = 0  
x = 65  
while a < 4:  
    i = 0
    while i < a + 1:
        print(chr(x), end=" ")  
        x = x + 1
        i = i + 1
    print()  
    a = a + 1
#output :-    A
#             B C
#             D E F
#             G H I J 

#Third way :- 
a = 0  
x = 65  
while a < 4:  
    i = 0  # Initialize i for the inner loop
    for i in range(a + 1):  # Loop through the required number of letters for the current row
        print(chr(x), end=" ")  
        x = x + 1  # Move to the next letter
    print()  
    a = a + 1
#output :-    A
#             B C
#             D E F
#             G H I J