for c in range (0,10):
    print (c) 
print('Fim')

contador =  1
while contador < 10:
    print(contador)
    contador= contador+1
print('Fim')
      
      
r= 'S'   
while r== 'S':
    n= int(input('Digite um número:'))
    r= str(input('Quer continuar? [S/N]')). upper()
print('Fim') 

n= 1
par= 0
impar= 0
while n!= 0:
    n= int(input('digite um número:'))
    if n!=0:
        if n%2== 0:
            par= par+1
        else:
            impar= impar+1
print('Você digitou {} números pares e {} números ímpares.'.format(par, impar))


    '''contador= contador+1
    if tentativa== 1:
        print('A soma dos valores {} e {} é de {}.'.format(v1,v2,s))
    elif tentativa== 2:
        print('A multiplicação dos valores {} e {} é de {}.'.format(v1,v2,m))
    elif tentativa== 3:
        if v1 > v2:
            print('O maior valor é {}.'.format(v1))
            if v1 < v2:
                print('O maior valor é {}.'.format(v2))
    elif tentativa== 4:
        tentativa= int(input('Informe um novo valor:'))
        tentativaII= int(input('Informe um novo segundo valor:'))
    elif tentativa== 5:
        print('Fim do programa!')
    else: 
        print('Essa opção não está disponível, tente novamente!')
print('Fim do programa!')''''''