n = 0
while True:
   n= int(input('Para saber a tabuada de x, digite um número:')) 
   if n < 0:
       break
   print(f'A tabuada do número {n} é dada por: ')
   for c in range (0,11):
       print(f'{n} * {c} = {n*c}')
print('Programa encerrado! Volte Sempre!')