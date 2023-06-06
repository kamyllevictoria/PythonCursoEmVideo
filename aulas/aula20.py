
def line (msg):
    print('-'*30)
    print(msg)
    print('-'*30)   
line('Desenvolvimento web')
line('Desenvolvimento mobile')


def soma (n1,n2):
    s = n1 + n2
    print(f'A soma de {n1} com {n2} é de {s}.')   
soma(4,5)
soma(4,6)
soma(8,9)


def contador(*numero):
    tamanho = len(numero)
    print(f'Recebi os valores {numero} e ao todo temos {tamanho} números.')
    for valor in numero:
        print(valor, end=' ')
    print('Fim.')     
contador(3,7,8,4,1)
contador(4,6,2)


def dobro_valores(lista):
    posição = 0
    while posição <len(lista):
        lista[posição] *= 2
        posição += 1
valores = [7,3,5,0,4]
dobro_valores(valores)
print(valores)
valores1 = [9,4,2,45,1]
dobro_valores(valores1)
print(valores1)


def soma_num(*valores):
    soma = 0
    for n in valores:
        soma += n
    print(f'Somando os valores {valores}, temos a soma {soma}.')
soma_num(5,2)
soma_num(5,2,9,3)