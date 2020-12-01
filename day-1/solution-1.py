data = open("input-1.txt", 'r')

data = list(map(lambda x: x.rstrip(), data.readlines()))

for i in range(data.__len__() - 1):

    first_parsed_num = int(data[i])

    for j in range(i + 1, data.__len__() - 1):
        second_parsed_num = int(data[j])

        if first_parsed_num + second_parsed_num == 2020:
            print(first_parsed_num, second_parsed_num, first_parsed_num * second_parsed_num)
