from itertools import combinations

data = open("input-2.txt", 'r')

data = list(map(lambda x: int(x.rstrip()), data.readlines()))

combs = list(combinations(data, 3))

for first, second, third in combs:

    if first + second + third == 2020:
        print(first, second, third, first * second * third)
