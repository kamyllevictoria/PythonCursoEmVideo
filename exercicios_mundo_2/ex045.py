from random import randint 
itens= ('Pedra', 'Papel', 'Tesoura')
computador= randint(0,2)
print('O computador escolheu {}.'.format(itens[computador]))
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador= int(input('Escolha sua jogada:'))
print('O computador escolheu {}.'.format(itens[computador]))
print('O jogador escolheu {}.'.format(itens[jogador]))
if computador== 0:
    if jogador== 0:
        print('Empatou!')
    elif jogador== 1:
        print('Jogador venceu!')
    elif jogador== 2:
        print('Computador venceu!')
    else:
        print('Jogada Inválida!')
elif computador== 1:
    if jogador== 0:
        print('Computador venceu!')
    elif jogador== 1:
        print('Empatou!')
    elif jogador== 2:
        print('Jogador venceu!')
    else: 
        print('Jogada Iválida!')            
elif computador== 2:
    if jogador== 0:
        print('Jogador venceu!')
    elif jogador== 1:
        print('Computador venceu!')
    elif jogador== 2:
        print('Empatou!')
    else: 
        print('Jogada Inválida!')