sorteio= []
temporaria= []
print('-=-'*30)
print('MEGASENA DA VIRADA')
print('-=-'*30)
from random import randint
num= int(input('Quantos jogos você quer que eu sorteie?'))
for v in range (1, num+1):
    for c in range(1,7):
        aleatorio= randint(1,60)
        temporaria.append(aleatorio)
    sorteio.append(temporaria[:])
    temporaria.clear()
for jogo in range (0,len(sorteio)):
    print(f'Jogo {jogo+1}: {sorteio[jogo]}')
print('-=-'*30)
print('BOA SORTE!')
print('-=-'*30)