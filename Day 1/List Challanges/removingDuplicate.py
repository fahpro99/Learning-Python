# delete duplicate items from a list

myList = [1, 2, 3, 1, 2, 3, 1, 2, 3]

l2 = []
for x in myList:
    if x not in l2:
        l2.append(x)
print(l2)

# concatenate all integer from a list to a single numbner

# l1 = [1, 2, 3, 4, 2, 2, 1, 12]

# s = ""
#
# for items in l1:
#     s += str(items)
#
# print(int(s))

# minimum index sum of two lists
# l1 = ['pizza', 'burger', 'hotdog', 'noodles', 'pasta', 'burger']
#
# l2 = ['burger', 'hotdog', 'noodles', 'pasta', 'nuggets', 'pizza']
#
# index1 = 10
# index2 = 10
#
# for i in range(len(l1)):
#     indx = l2.index(l1[i])
#     if i + indx < index1 + index2:
#         index1 = i
#         index2 = indx
#
# print(l1[index1], index1 + index2)

# oerlapping elements of two lists

l1 = [10, 14, 15, 1, 13, 9, 0]
l2 = [14, 6, 9, 4, 7, 1, 0, 13]
l3 = []
for items in l1:
    if items in l2:
        l3.append(items)
print(l3)
