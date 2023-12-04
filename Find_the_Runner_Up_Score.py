n = int(input())
arr = map(int, input().split())

sort_arr = set(sorted(arr))
print(list(sort_arr)[-2])
