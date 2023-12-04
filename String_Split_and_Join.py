def split_and_join(line):
    sentence_split = line.split(" ")
    sentence_join = "-".join(sentence_split)
    return sentence_join

line = input()
result = split_and_join(line)
print(result)
