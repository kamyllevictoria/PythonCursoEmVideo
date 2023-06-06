contador= 0
n= int(input('Informe um número:'))
for c in range (1, n+1):   
    if n%c== 0:
        print('\033[34m', end='')
        contador= contador+1        
    else:
        print('\033[m', end='')
    print('{}'.format(c), end=' ')
print('O número {} foi divisível {} vezes.'.format(n,contador))

