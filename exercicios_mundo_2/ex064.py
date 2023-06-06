soma= 0
contador= 0
n= int(input('Digite um número [999 para parar]:'))
while n !=999:
    soma= soma+ n
    contador= contador+ 1
    n= int(input('digite um número [999 para parar]:'))
print('Você digitou {} números e a soma entre eles é de {}.'.format(contador, soma))