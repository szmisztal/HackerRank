def count_substring(string, sub_string):
    list_to_count = []
    for i in range(len(string)):
        if sub_string in string[0 + i:len(sub_string) + i]:
            list_to_count.append(sub_string)
    return len(list_to_count)

string = input().strip()
sub_string = input().strip()

count = count_substring(string, sub_string)
print(count)
