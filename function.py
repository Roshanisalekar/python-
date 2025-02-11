# program : 1
def sachin():
    a=int(input("enter a no 1 :"))
    b =int(input("enter a no 2 :"))
    c =int(input("enter a percentage: "))
    final=(a+b)*c/100
    print(final)
sachin()

"""
output :
enter a no 1 :24
enter a no 2 :24
enter a percentage: 10
4.8
"""

#program :2

def nida(a,b,c):
    final=(a+b)*c/100
    print(final)
    
nida(123,123,10)
nida(2000,2000,10)

"""
output :
24.6
400.0
"""

# program:3 

def roshani(n):
    rev=0
    while(n>0):
        rem=n%10
        rev=(rev*10)+rem
        n=n//10
    print(rev)

roshani(2461)

"""
output :

1642
"""

#program:4
def greet(a):
    print(f"hello user {a}")
    
                                   #formulastring
greet("raj")

"""
output :

hello user raj
"""

# program :5

def greet():
    a=str(input("enter a name :"))
    print(f"hello user {a}")
greet()
    
"""
output :

enter a name :roshani
hello user roshani
"""

# program :6
def user():
    salary=int(input("enter a salary :"))
    b=int(input("enter a p f :"))
    c =int(input("enter a ESIC :"))

    d=b+c 
    final=salary*d//100
    total=salary-final
    print(total)
    print("mandal abhari aahe")
user()

"""
output:

enter a salary :50000
enter a p f :12
enter a ESIC :8
40000
mandal abhari aahe
"""
# program :7

# 1 way 

def volumeofshpere():
    r=float(input("enter a radius :"))
    vol=(4/3)*3.14*r*r*r
    print(vol)
volumeofshpere()

"""
output:

enter a radius :12
7234.559999999999
""""
# 2 way 

def volumeofsphere():
    radius=int(input("enter the radius :-   "))
    volume=(4/3)*(22/7)*(radius**3)
    print(f'volume of sphere is {volume} cubic units')
volumeofsphere()

"""
output :

enter the radius :-   12
volume of sphere is 7241.142857142856 cubic units

"""
