from collections import Counter

xd = int(input())
nums = list(map(int, input().split()))

sizes = Counter(nums)
n = int(input())
gains = 0
for i in range(n):
    shoe_size, price = map(int, input().split())
    if shoe_size in sizes.keys():
        if sizes[shoe_size] > 0:
            gains += price
            sizes[shoe_size] -= 1

print(gains)
