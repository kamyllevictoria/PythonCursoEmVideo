# def ficha (player='<Desconhecido>', points=0):
#     return f'The name of player is {player} and scored {points} points.'

# # def line():
# #     print('-'*45)
# # line()
# # player1 = ficha('Lucas', 10)
# # print(player1)
# # line()
# # player2 = ficha('ana')
# # print(player2)
# # line()
# # print('Now, its your time to inform the name and the points of your favorite football player!')

# n = str(input('Name: '))
# g = str(input('Gols: '))

# if g.isnumeric():
#     g = int(g)
# else:
#     g = 0
    
# if n.strip() == '':
#     ficha(points = g)
# else: 
#     ficha(n, g)

# # line()
# player3 = ficha(n, g)
# print(player3)
# # line()

def ficha(jogador='<desconhecido', pontos=0):
    print(f'O jogador {jogador} fez {pontos} pontos no campeonato')

nome = str(input('Digite o nome do jogador: '))
gols = str(input('Numero de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    g = 0
    
if nome.strip() == '':
    ficha(pontos = gols)
else:
    ficha(nome, gols)
    
        
