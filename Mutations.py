def mutate_string(string, position, character):
    list_string = list(string)
    list_string[position] = character
    new_word = "".join(list_string)
    return new_word

s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)

