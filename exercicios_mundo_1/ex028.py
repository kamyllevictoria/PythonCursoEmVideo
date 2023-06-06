import random
print('Vamos fazer um jogo! Quero ver se você conseguirá advinhar o número em que estou pensando.')
n1= int(input('Digite um número:'))
lista= [0,1,2,3,4,5]
numero= random.choice(lista)
if n1== numero: 
    print('Parabéns, você acertou!')
else: 
    print('Não foi dessa vez!')