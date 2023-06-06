def count(phrase):
    upperCase=0
    lowerCase=0
    for letter in phrase:
        if letter.islower():
            lowerCase+=1
        elif letter.isupper():
            upperCase+=1
    return lowerCase,upperCase

myPhrase='Fahim Anwar'
counter=count(myPhrase)
print(counter)
