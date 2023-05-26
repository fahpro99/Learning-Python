food = ['pizza', 'nuggets', 'hotdog', 'noodles', 'pasta', 'burger']
myInput = input("Your input is\n")
result = []
for items in food:
    if items.startswith(myInput):
        result.append(items)
print(result)
