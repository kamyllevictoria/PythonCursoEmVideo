n1= int(input('Digite um número para realizar a conversão de bases:'))
print('''Escolha uma das bases para conversão:
[1] converter para binário
[2] converter para octal
[3] converter para hexadecimal''')
e= int(input('Sua opção é:'))
if e== 1:
    print('{} convertido para binário é igual a {}.'. format(n1,bin(n1)))
elif e==2:
    print('{} convertido para octal é igual a {}.'. format(n1,oct(n1)))
elif e==3:
    print('{} convertido para hexadecimal é {}.'.format(n1,hex(n1)))