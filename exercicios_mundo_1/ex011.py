n1=int(input('Olá, boa tarde, você ligou para a Casa de Pintura L&K, para saber a quantidade de tinta necessária para pintar seu cômodo, informe a altura da parede desejada, por favor:'))
n2=int(input('Muito obrigado pela colaboração, agora digite o comprimento da parede:'))
a= n1*n2
lt= (n1*n2)/2
print('A área informada, conforme os dados da altura e comprimento, é de {}, logo, será preciso {} latas de tinta para realizar a pintura completa.'.format (n1*n2,(n1*n2)/2))