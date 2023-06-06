import random 
n1= int(input("Digite um número"))
r= n1%2 
print('O resultado foi de {}.'. format(r))
if r== 0:
    print('O número {} é par.'. format(n1))
else: 
    print('O número {} é ímpar.'.format(n1))    