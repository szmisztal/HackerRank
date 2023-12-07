from string import ascii_lowercase

def print_rangoli(size):
    for i in range(size-1, 0, -1):
        line = '-'.join(ascii_lowercase[size-1:i:-1] + ascii_lowercase[i:size])
        print(line.center(size * 4 - 3, "-"))

    for i in range(size):
        line = '-'.join(ascii_lowercase[size-1:i:-1] + ascii_lowercase[i:size])
        print(line.center(size * 4 - 3, "-"))


n = int(input())
print_rangoli(n)
