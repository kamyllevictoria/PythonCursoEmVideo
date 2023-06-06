from random import randint
from operator import itemgetter
dados = {'jogador 1': randint(1,6),
         'jogador 2': randint(1,6),
         'jogador 3': randint(1,6),
         'jogador 4': randint(1,6)}
# print(dados)
for k, v in dados.items():
    print(f'{k} tirou o valor {v}')
    
ranking = list()
ranking = sorted(dados.items(), key = itemgetter(1), reverse = True)

# print(ranking)
print('-'*30)
print('RANKING DOS JOGADORES')
print('-'*30)

for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]} pontos')