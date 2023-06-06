from random import randint
print('Bem vindo ao jogo! Vamos ver se você conseguirá ganhar uma partida!')
jogador = int(input('Faça sua jogada com base nos números [1,2,3,4,5,6,7,8,9,10]: '))
while True:
    itens = ['1','2','3','4','5','6','7','8','9','10']
    print(f'O jogador escolheu o número {jogador}')
    computador = randint (0,10)
    print(f'O computador escolheu o número {itens[computador]}')    
    if jogador < computador:
        break
    elif jogador == computador:
        print("O jogo empatou, tente novamente!")
    elif jogador >= computador:
        print('Parabéns, você ganhou o jogo!')
print('Poxa vida, você perdeu! Fim da partida.')