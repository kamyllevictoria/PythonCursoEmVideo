a= int(input('Digite um número:'))
b= int(input('Digite um segundo número:'))
c= int(input('Digite um terceiro número:'))
if a<c and a<b:
    menor= a
if b<a and b<c:
    menor= b
if c<a and c<b:
    menor= c
print('O menor valor digitado foi {}.'.format(menor))