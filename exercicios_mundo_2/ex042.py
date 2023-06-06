print ('-='*20)
print('Analisador de Triângulos:')
print('-='*20 ) 
r1= float(input('Digite um comprimento de reta:')) 
r2= float(input('Digite um segundo comprimento de reta:'))
r3= float(input('Digite um terceiro comprimento de reta'))
if r1==r2==r3:
    print('O triângulo é equilátero.')
elif (r1==r2)!=r3:
    print('O triângulo é isóceles.')
elif r1!=r2!=r3:
    print('O triângulo é escaleno.')