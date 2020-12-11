from functools import reduce
from operator import mul

raw_data = open('day-3\\input-1.txt', 'r').readlines()

data = list(map(lambda x: x.rstrip(), raw_data))

options = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]

results = []

for option in options:

    pos = (0, 0)

    tree_count = 0

    while pos[1] < len(data):

        symbol = data[pos[1]][pos[0]]

        if symbol == '#':
            tree_count = tree_count + 1

        pos = ((pos[0] + option[0]) % len(data[0]), pos[1] + option[1])

    results.append(tree_count)

print(reduce(mul, results, 1))
