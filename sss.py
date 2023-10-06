import math
import random

print(math.pow(2,10))
print(2**10)
print([1,2.3]*3)
print({x:x*x for x in range(1,100)})
for i in range(5):
    print(i)
else:
    print("d")

dicc={'a':1,}

print(dicc.keys())
def funcion(country='francia'):
    print("hola",country)

funcion("spain")
funcion("")
funcion()

x=5
y=1+(20 if x< 5 else 30)
print(y)



x=1j
print(x**2==-1)