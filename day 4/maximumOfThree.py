def max3(a,b,c):
    if a>b and a>c:
        return a

    elif b>c:
        return b
    else:
        return c
print(max3(17,25,99))