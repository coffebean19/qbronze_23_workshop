from random import randrange

def biased_coin(N,B):
    from random import randrange
    random_number = randrange(N)
    if random_number < B:
        return "Heads"
    else:
        return "Tails"
    
N = 101
B = randrange(N+1)

total_tosses = 500
heads = 0

for i in range(total_tosses):
    if biased_coin(N,B) == "Heads":
        heads = heads + 1

guess = heads/total_tosses
real_bias = B/N
error = abs(guess-real_bias)/real_bias*100

print("my guess is",guess)
print("real bias is", real_bias)
print("error (%) is",error)