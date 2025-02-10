#Loop 05-01-2025
#1) Program :-
for i in range(1,5,1):
    for j in range(i,5,1):
        print("*",end=" ")
    print()
#output :- * * * * 
#          * * * 
#          * * 
#          * 

#2) Program :-
for i in range(1,6,1):
    for j in range(i,6,1):
        print(" ",end=" ")
    for k in range(0,i):
        print("*",end=" ")
    print()
#output :-   * 
#          * * 
#        * * * 
#      * * * * 
#    * * * * *

#3) Program :-
for i in range(1,6,1):
    for j in range(i,6,1):
        print(" ",end=" ")
    for k in range(0,i):
        print("*",end=" ")
    for l in range(1,i):
        print("*",end=" ")
    print()
#output :-       * 
#              * * * 
#            * * * * * 
#          * * * * * * * 
#        * * * * * * * * *

#4) Program :-
for i in range(1,6,1):
    for j in range(i,6,1):
        print(" ",end=" ")
    for k in range(0,i):
        print("*",end=" ")
    for l in range(1,i):
        print("*",end=" ")
    print()
for q in range(1,5,1):
    for m in range(-1,q):
        print(" ",end=" ")
    for n in range(q,5,1):
        print("*",end=" ")
    for o in range(q,4):
        print("*",end=" ")
    print()
#output :-                        * 
#                               * * * 
#                             * * * * * 
#                           * * * * * * * 
#                         * * * * * * * * * 
#                           * * * * * * * 
#                             * * * * * 
#                               * * * 
#                                 *

#5) Program :-
for i in range(1,5):
    for j in range(i,5):
        print("*",end=" ")
    for k in range(1,i):
        print("-",end=" ")
    for l in range(1,2):
        print("0",end=" ")
    print() 
for a in range(1,4):
    for b in range(-1,a):
        print("*",end=" ")
    for c in range(a,3):
        print("-",end=" ")
    for d in range(1,2):
        print("0",end=" ")
    print()
for x in range(1,4):
    for y in range(x,4):
        print("*",end=" ")
    for z in range(0,x):
        print("-",end=" ")
    for w in range(1,2):
        print("0",end=" ")
    print() 
for i in range(1,6):   
    print("0",end=" ")
#output :-      * * * * 0 
#               * * * - 0 
#               * * - - 0 
#               * - - - 0 
#               * * - - 0 
#               * * * - 0 
#               * * * * 0 
#               * * * - 0 
#               * * - - 0 
#               * - - - 0 
#               0 0 0 0 0                      