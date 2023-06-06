def planet(id):
    planets={1:'Mercury',2:'Venus',3:'Earth',4:'Mars',5:'Jupiter',6:'Saturn',7:'Uranus',8:'Neptune',9:'Pluto'}
    if abs(id<=9):
        return planets[id]
    else:
        print('Invalid Id')
p=planet(5)
print(p)