from itertools import product

x = int(input())
y = int(input())
z = int(input())
n = int(input())

started_list = [[x for x in range(0, x + 1)], [y for y in range(0, y + 1)], [z for z in range(0, z + 1)]]

all_combinations = [list(combination) for combination in product(*started_list)]

filtered_combinations = []
for element in all_combinations:
    if sum(element) != n:
        filtered_combinations.append(element)
print(filtered_combinations)

