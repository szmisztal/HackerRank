n = int(input())
integers = input().split()
print(all([int(i) > 0 for i in integers]) and any([i == i[::-1] for i in integers]))
