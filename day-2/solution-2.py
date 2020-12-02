from collections import Counter


input = open("input-2.txt", "r")

parsed_data = list(map(lambda x: x.rstrip(), input.readlines()))

valid_texts = 0

for item in parsed_data:
    tokens = item.split(' ')

    positions = tokens[0].split('-')

    first_position = int(positions[0])

    second_position = int(positions[1])

    letter = tokens[1][0]

    main_text = tokens[2]

    if (main_text[first_position - 1] == letter) ^ (main_text[second_position - 1] == letter):
        print(item)
        valid_texts = valid_texts + 1

print(valid_texts)
