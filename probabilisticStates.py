# import random

# states = []
# total = 0

# for i in range(4):
    # states.append(random.randint(0,1000))
    # total += states[i]

# #Normalize
# for i in range(4):
    # states[i] = round(states[i]/total, 2)

import random

A = [[0,0,0],
     [0,0,0],
     [0,0,0]]

norm_factor = [0,0,0]

for j in range(3):
    norm_factor[j] = 0
    while norm_factor[j] == 0:
        for i in range(3):
            A[i][j] = random.randrange(101)
            norm_factor[j] += A[i][j]

print("matrix A before normalization:")
for i in range(3):
    print(A[i])

#Normalization
for j in range(3):
    for i in range(3):
        A[i][j] /= norm_factor[j]

#Matrix A after normalization
print()
print("Matrix A after normalization")
for i in range(3):
    print(A[i])

sum = [0,0,0]
for j in range(3):
    for i in range(3):
        sum[j] += A[i][j]

print(sum)


B = [[0.4,0.6,0],
     [0.2,0.1,0.7],
     [0.4,0.3,0.3]
    ]
#Current state
v = [0.1,0.3,0.6]

newstate = []

index = 0

for row in B:
    newstate.append(0)
    for i in range(len(row)):
        newstate[index] = newstate[index] + row[i] * v[i]
    index += 1
    
print(newstate)