def sumo(l):
    s=0
    for i in l:
        if i%10==0:
            s+=i
    return s
list=[45,67,23,123,100,200]
print(sumo(list))
