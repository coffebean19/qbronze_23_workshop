# # import random

# # states = []
# # total = 0

# # for i in range(4):
#     # states.append(random.randint(0,1000))
#     # total += states[i]

# # #Normalize
# # for i in range(4):
#     # states[i] = round(states[i]/total, 2)

# import random

# A = [[0,0,0],
#      [0,0,0],
#      [0,0,0]]

# norm_factor = [0,0,0]

# for j in range(3):
#     norm_factor[j] = 0
#     while norm_factor[j] == 0:
#         for i in range(3):
#             A[i][j] = random.randrange(101)
#             norm_factor[j] += A[i][j]

# print("matrix A before normalization:")
# for i in range(3):
#     print(A[i])

# #Normalization
# for j in range(3):
#     for i in range(3):
#         A[i][j] /= norm_factor[j]

# #Matrix A after normalization
# print()
# print("Matrix A after normalization")
# for i in range(3):
#     print(A[i])

# sum = [0,0,0]
# for j in range(3):
#     for i in range(3):
#         sum[j] += A[i][j]

# print(sum)


# B = [[0.4,0.6,0],
#      [0.2,0.1,0.7],
#      [0.4,0.3,0.3]
#     ]
# #Current state
# v = [0.1,0.3,0.6]

# newstate = []

# index = 0

# print()
# for row in B:
#     newstate.append(0)
#     print(newstate)
#     for i in range(len(row)):
#         newstate[index] = newstate[index] + row[i] * v[i]
#         print(newstate[index])
#     index += 1
    
# print()
# print(newstate)

def linear_evolve(operator, state):
    newstate=[]
    for i in range(len(operator)):
        newstate.append(0)
        for j in range(len(state)):
            newstate[i] = newstate[i] + operator[i][j] * state[j]
    return newstate

B = [
    [0.4,0.6,0],
    [0.2,0.1,0.7],
    [0.4,0.3,0.3]
]

v = [0.1, 0.3, 0.6]

newstate = linear_evolve(B,v)
print(newstate)

for step in [5, 10, 20, 40]:
    new_state = [1, 0, 0] #initial state
    for i in range(step):
        new_state = linear_evolve(B, new_state)
    print(new_state)