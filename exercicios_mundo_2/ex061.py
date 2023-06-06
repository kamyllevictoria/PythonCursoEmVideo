a1= int(input('Digite o primeiro termo da pa:'))
razão= int(input('Digite a razão da pa:'))
termo= a1
contador= 1
while contador<= 10:
    print('{}'.format(termo), end='-')
    termo= termo+ razão
    contador= contador+ 1
print('Fim da p.a!')