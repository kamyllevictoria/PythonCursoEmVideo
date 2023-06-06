'''contador = 1
while contador <= 10:
    print(contador, '->', end='')
    contador = contador + 1
print('Acabou!')'''

n = 0
soma = 0
while True:
    n= int(input('Digite um número:'))
    if n == 999:
        break
    soma = soma + n
print(f'A soma vale {soma}.') 