km= int(input('Qual é a distância que será percorrida na viagem?'))
print('A distância percorrida será de {}km.'.format(km))
p1= km*0.5
p2= (km-200)*0.45+200*0.5
if km>= 200:
    print('A distância percorrida custará {:2f} reais.'. format(p2))
else:
    print('A distância percorrida custará {:2f} reais.'. format(p1))