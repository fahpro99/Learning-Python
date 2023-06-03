print('Hello')
dict1={101:'john',102:'matthew',103:'messi'}
print(dict1)



for i in dict1:
    print(i,dict1[i])

# dictionary Comprehension

dict2=dict()
dict2['apple']='red'
dict2['mango']='yellow'

for x in range(1,5):
    dict2[x]=x**2
print(dict2)

dict3=dict(((1,2),(2,4),(3,6)))
dict2=dict(([1,11],[2,22],[3,33]))
print(dict2)

dict2=dict(('ab','cd','ef'))
print(dict2)
# dict2=dict(([1,11,12],[2,22,23],[3,33,34]))
# triplet is not allowed
print(dict2)

l1=['A','B','C']
l2=['Apple','Ball','Cat']

dict3=dict(zip(l1,l2))
print(dict3)


l1=[10,20,30]

dict4=dict(enumerate(l1))
print(dict4)

dict6={x for x in range (1,11)}

dict6={x:x**2 for x in  range (1,6)}
print(dict6)
l1=[1,2,3]
s1={'kamal','jamal','rahman'}

dict7={x:y for x,y in zip(l1,s1)}
print(dict7)

dict8={x:y for x,y in enumerate(s1)}
print(dict8)

#looping through a dictionary

for x in dict7:
    print(x,dict7[x])
for x in dict7:
    print(x,dict7.get(x))

# print(dict7[5]) gives error

# print(dict7.get(x),"invalid key") gives no error rather handeling exception

print(dict7.keys())
print(dict7.values())
print(dict7.items())

for x in dict7.keys():
    print(x)
for x in dict7.values():
    print(x)
for x,y in dict7.items():
    print(x,y)

dict1={101:'production',102:'Sales & Marketing'}
dict2=dict1.copy()

dict2[102]='Designing'
print(id(dict1[102]))
print(id(dict2[102]))

l1=[11,22,33,44]
dict3={}
dict3=dict3.fromkeys(l1,'hello')#assigning the hello to every key
print(dict3)
dict3=dict3.pop(50,'none')
print(dict3)