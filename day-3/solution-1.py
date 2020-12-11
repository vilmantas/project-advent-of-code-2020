raw_data = open('day-3\\input-1.txt', 'r').readlines()

data = list(map(lambda x: x.rstrip(), raw_data))

pos = (0, 0)

tree_count = 0

while pos[1] < len(data):

    symbol = data[pos[1]][pos[0]]

    if symbol == '#':
        tree_count = tree_count + 1

    pos = ((pos[0] + 3) % len(data[0]), pos[1] + 1)

print(tree_count)
