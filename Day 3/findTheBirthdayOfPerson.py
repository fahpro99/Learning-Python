birthdays={
    'sachin':'3/14/2003',
    'carl':'1/17/1',
    'khan':'12/10/2006',
    'donald':'6/14/2010',
    'rohan':'1/6/2005'
}
flag='t'
for x in birthdays:
    print(x)
while(flag=='t'):
    name=input("Which name do you want to find ?\n")
    print(birthdays.get(name))
    flag=input('Do you want to search again? y or n\n')
print('Thank you')
