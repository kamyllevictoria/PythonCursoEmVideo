v= int(input('Digite a velocidade atual do seu carro em km/h:'))
print('A velocidade atual do seu carro é de {}km/h.'. format(v))
v1= (v-80)*7
if v>=80: 
    print('O seu limite de velocidade excedeu o estabelecido, logo, o senhor está sujeito a uma multa de {} reais'. format(v1))
else:
    print('O seu limite de velocidade é adequado. Tenha uma boa viagem.')