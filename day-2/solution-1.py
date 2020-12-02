from collections import Counter


input = open("input-1.txt", "r")

parsed_data = list(map(lambda x: x.rstrip(), input.readlines()))

valid_texts = 0

for item in parsed_data:
    tokens = item.split(' ')

    limits = tokens[0].split('-')

    min = int(limits[0])

    max = int(limits[1])

    letter = tokens[1][0]

    main_text = tokens[2]

    counts = Counter(main_text)

    if counts[letter] >= min and counts[letter] <= max:
        print(item)
        valid_texts = valid_texts + 1

print(valid_texts)
