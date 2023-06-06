def addItem(item,l=[]):
    l.append(item)
    return l
l1=[5,4,62,23,11]

print(addItem(5,l1))

# Variable length arguments
def fun1(*args):
    print(type(args),args)
fun1('jayem','sarkar')
fun1()
fun1('Fahim','Ahnaf','Saikha')

# unpacking arguments
def fun2(a,b,c):
    print(a,b,c)

l1=[11,22,33]
fun2(*l1)
#if we pass star then it will give no error

#multiple return values

def fun3(a,b,c):
    return a+1,b+1,c+1

print(fun3(1,2,3))

#variable length keyword arguments
def fun4(**kwargs):
    print(kwargs)

fun4(name='fahim anwar',id='20-42305-1',sec='A')
# iterator function

l=[1,2,3,4,5]
itr=iter(l)

print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))


# cyclic generator of our own

def days():
    l=['sat','sun','mon','tues','wed','thurs','fri']
    i=0
    while True:
        x=l[i]
        i=(i+1)%7
        yield x
d=days()
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))

# global variable using

# a function cannot modify global unless using global inside a function
g=10

def funny():
    global g
    g=g+10
    print('global',g)
funny()
print('gloal',g)

# recursive function

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

x=fact(5)
print(x)
#Build in fucntions


#absolute function
f=abs(3+4j)#3^2+4^2
print(f)

# Ascii
s1='abcde'
ba=bytearray(s1.encode())
for i in ba:
    print(i)

dc=ba.decode()
print(dc)
#byte array muteable bytes are not mutable

#callable function ensures that it is function or not
print(chr(97))
print(ord('a'))

print(dir(str))
print(divmod(13,2))

l=['a','b','c']
e=enumerate(l)
for i in e:
    print(i)

evalu=eval('2+2')
print(evalu)

s='x=10\ny=20\nprint(x+y)'
exacc=exec(s)



l=[3,6,7,9,12,14,19,21]

def even(x):
    if x%2==0:
        return  True
    else:
        return False
f=filter(even,l)
for i in f:
    print(i)


f=12.546
s=format(f,'E')
print(s)

fz=frozenset(l)
print(fz)


s='abcde'


print(hash(s))
print(help(s.isdigit()))


l1=[1,2,3,4,5]
m=map(lambda x:x**2,l1)
print(list(m))
l2=[5,4,3,2,1]
m1=map(lambda x,y:x+y,l1,l2)
print(list(m1))

print(sorted(l1,reverse=True))