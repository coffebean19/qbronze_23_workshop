import maths
from random import randrange

u = []
v = []

for i in range(10):
    u.append(randrange(1,10))
    v.append(randrange(0,10))

print("Vector u:",u)
print("Vector v:",v)
print()
print("Sum of vector u and v:", maths.vector_Sum(u,v))
