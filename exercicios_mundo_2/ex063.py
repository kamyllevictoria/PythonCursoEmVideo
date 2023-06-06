n= int(input('Quantos números você quer inserir na Sequência de Fibonacci?'))
print('{} números.'.format(n))
t1= 0
t2= 1
print('{}-{}'.format(t1,t2),end='-')
contador= 3
while contador <=n:
    t3= t1+t2
    contador= contador+ 1
    print('-{}.'.format(t3),end='-')
    t1= t2
    t2= t3
print('Fim')