a1= int(input('Informe o primeiro termo da p.a:'))
r= int(input('Informe a razão da p.a:'))
a10= a1+(10-1)*r
for c in range (a1,a10,r):
    print('{}'.format(c), end=' ')
print('Acabou.')