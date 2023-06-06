def invDict(d):
    newd={}
    for k,v in d.items():
        newd[v]=k
    return newd
dic={'ajay':10,'fahim':201,'selim':20}
print(invDict(dic))