print('Vamos ver se o seu número é primo!')
n= int(input('Informe um número:'))
total= 0
for c in range(1,n):
    if n%c== 0:
        print(end='')
        total= total+1
    else: 
        print(end='')
    print('{}'. format(c), end='')
print('O número {} foi divisível por {} vezes.'.format(n, total))
if total== 2:
    print ('Por isso ele é primo.')
else:
    print('Por isso ele não é primo.')


