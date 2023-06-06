d1=float(input('Olá, você ligou para a concessionária L, para alugar um carro, digite o número de dias que irá utilizá-lo:'))
km1= float(input('Para auxiliar na seleção do veículo e calcular os custos finais, informe a quilometragem que será percorrida:'))
d=d1*60
km=km1*0.15
print('O custo para reservar um carro econômico por um período de {} dias, é de {} reais, já o custo para percorrer a quilometragem informada é de {} reais.'. format(d1, d1*60, km1*0.15))
