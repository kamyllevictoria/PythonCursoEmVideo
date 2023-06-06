cmaior=0
cmenor= 0
for pessoa in range(1,8):
    ano= int(input('Em qual ano a {} pessoa nasceu?'.format(pessoa)))
    maioridade= 2023-ano
    if maioridade >= 18:
        cmaior= cmaior+1
    else:
        cmenor= cmenor+1
print('O total de pessoas maiores de idade é de {} e o total de menores de idade é de {}'.format(cmaior, cmenor))