v1= int(input('Informe um valor:'))
v2= int(input('Informe um segundo valor:'))
opção= 0
while opção != 5:   
    print('''      [1] somar  
      [2] multiplicar 
      [3] maior número
      [4] novos números 
      [5] sair do programa''')
    opção= input('Selecione uma opção:')
    if opção== 1:
       soma= v1+v2 
       print('A soma entre {} e {} é de {}.'.format(v1,v2,soma))
    elif opção== 2:
        multiplicação= v1*v2
        print('A multiplicação entre {} e {} é de {}.'.format(v1,v2,multiplicação))
    elif opção== 3:
        if v1> v2:
            print('O maior número é {}.'.format(v1))
        if v2> v1:
            print('O maior número é {}.'.format(v2))
        if v2==v1:
            print('Os números {} e {} são iguais.'.format(v1,v2))
    elif opção== 4:
        print('Escreva os números novamente:')
        v1= int(input('Informe um valor:'))
        v2= int(input('Informe um segundo valor:'))
    elif opção== 5:
        print('Finalizando...')
else:
    print('Não foi possível realizar a operação, tente novamente!')