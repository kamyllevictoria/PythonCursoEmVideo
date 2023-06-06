total18 = 0 
totalh = 0
totalm = 0
while True:
    idade = int(input('Idade:'))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo: [F/M]')).upper().strip()
    if idade >= 18:
        total18 = total18 + 1
    if sexo == 'H':
        totalh = totalh + 1
    elif sexo == 'M' and idade < 20:
        totalm == totalm + 1
   
   
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N]')).upper().strip()
    if resposta == 'N':
        print('Acabou!')
        print(f'O total de pessoas com mais de 18 anos é de {total18}')
        print(f'O total de homens cadastrados é de {totalh}')
        print(f'O total de mulheres com menos de 20 anos cadastradas é de {totalm}')