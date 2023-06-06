contador = 0
soma = 0
n1 = 0
while True:
    n1= int(input('Digite um número:'))
    contador = contador + 1
    if n1 == 999:
        break 
    soma = soma + n1
print(f'Você informou {n1} números e a soma entre eles é de {soma}')