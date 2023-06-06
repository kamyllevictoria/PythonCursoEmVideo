a= int(input('Digite um ano:'))
a1= a%4
if a1== 0:
    print('O ano {} é bissexto.'.format(a))
else:
    print('O ano {} não é bissexto.'. format(a))