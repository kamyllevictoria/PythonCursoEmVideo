import math
print ('-='*20)
print('Analisador de Triângulos:')
print('-='*20 ) 
r1= float(input('Digite um comprimento de reta:')) 
r2= float(input('Digite um segundo comprimento de reta:'))
r3= float(input('Digite um terceiro comprimento de reta'))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('Os segmentos acima podem formar um triângulo.')
else:
    print('Os segmentos acima não podem formar um triângulo.')