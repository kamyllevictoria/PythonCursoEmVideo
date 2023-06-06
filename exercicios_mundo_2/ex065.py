resposta = 'S'
contador = 0
soma = 0
media = 0
n = int(input('Digite um número:'))
while resposta in 'Ss':
    n = int(input('Digite um número:'))
    contador = contador + 1
    soma = soma + n
    resposta = str(input('Deseja continuar com a operação? [S/N]')).upper().strip()
media = soma/ contador
print('Você digitou {} números e a média entre elses é de {}.'.format(contador, media))
