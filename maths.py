def vector_Sum(u, v):
    result = []
    for i in range(len(u)):
        result.append(u[i] + v[i])
    return result

u = [1, 2, 4, 5]
v = [3, 0, 2, 1]

print(vector_Sum(u, v))