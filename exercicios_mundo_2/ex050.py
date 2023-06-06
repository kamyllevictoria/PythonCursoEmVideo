soma= 0
contador= 0
for c in range (1,7):
    n= int(input('Digite um valor:'.format(c))) 
    if n % 2== 0:
        soma= soma+n
        contador= contador+1
print('Você informou {} números e sua soma foi de {}.'. format (c,soma))