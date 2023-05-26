l1 = ['A', 'B', 'C', 'D', 'E', 'F', 'B', 'C', 'F', 'E', 'A', 'B', 'A', 'B']

result = []

for items in l1:
    cnt = l1.count(items)

    if (items, cnt) not in result:
        result.append((items, cnt))
print(result)
