from random import randint
computador= randint(0,10)
print('Sou seu computador e acabei de pensar em um número. Será que você consegue advinhar?')
acertou= False
tentativas= 0
while not acertou:
   jogador= int(input('Qual é seu palpite?')) 
   tentativas= tentativas+ 1
   if jogador== computador:
       acertou= True
   else:
       if jogador < computador:
           print('Mais')
       elif jogador > computador:
           print('Menos')
print('Você acertou!')
print('Suas tentativas até acertar foram de {} vezes'.format(tentativas))
