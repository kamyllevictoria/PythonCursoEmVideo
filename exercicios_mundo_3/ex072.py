escrita ='zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatrorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove'
print(escrita)
while True:
    n1 = int(input('Digite um número no intervalo de 1-20:'))   
    if 0 <= n1 <= 20:
        break
    print('Tente novamente.')
print(f'Você digitou o número {escrita[n1]}')