dados = {}
partidas = []

dados ['Jogador'] = str(input('Digite o nome do jogador: '))
total = int(input(f'Digite quantas partidas o jogador {dados["Jogador"]} participou: '))
for c in range (1, total):
    partidas.append(int(input(f'Quantos pontos o jogador fez em na partida {c}? ')))

dados ['Gols'] = partidas[:]
dados['Total de pontos'] = sum(partidas)
# print('-'*30)
# print(dados)
# print('-'*30)
print(f'O jogador {dados["Jogador"]} jogou {total} partidas')
print(f'O jogador {dados["Jogador"]} obteve um total de {dados["Total de pontos"]} pontos em todas as partidas. ')