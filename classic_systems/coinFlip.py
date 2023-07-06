from random import randrange

for experiment in [100, 1000, 10000, 100000]:
    heads = tails = 0
    for i in range(experiment):
        if randrange(2) == 0: heads = heads + 1
        else: tails = tails + 1
    print("experiment:", experiment)
    print("head =", heads," tails = ",tails)
    print("the ratio of #heads/#tails is",(round(heads/tails, 4)))
    print() #empty line