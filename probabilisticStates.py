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
