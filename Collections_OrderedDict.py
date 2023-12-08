from collections import OrderedDict
n = int(input())
items_sold = OrderedDict()
for i in range(n):
    item_name, net_price = input().rsplit(" ", 1)
    if item_name in items_sold:
        items_sold[item_name] += int(net_price)
    else :
        items_sold[item_name] = int(net_price)
[print(i, items_sold[i]) for i in items_sold]
