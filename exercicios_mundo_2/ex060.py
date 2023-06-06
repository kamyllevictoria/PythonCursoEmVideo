num= int(input('Digite um número para saber seu fatorial!'))
resultado= 1
contador= 1
while contador <= num:
    resultado= resultado*contador
    contador= contador+1
print('O fatorial do número {} é de {}'.format(num,resultado))