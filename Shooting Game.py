al=int(5)
ml=int(3)
while True:
    x = input()
    if x == 'exit':
        break
    elif x == 'gun':
      ml-=1
      if ml==0:
        print('Monster killed')
        break
      else:
        print('Monster has ' + str(ml) + ' lives')
    elif x == 'laser':
      al-=1
      if al==0:
        print('Alien killed')
        break
      else:
        print('Alien has ' + str(al) + ' lives')
