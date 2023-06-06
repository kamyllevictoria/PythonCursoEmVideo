valor = int(input('Olá, bem vindo ao banco K, para realizar um saque, informe o valor desejado:'))
total = valor 
cédula = 50
contador = 0 
while True:
    if  total >= cédula:
        total = total - cédula 
        contador = contador + 1
    else:
        print(f'Total de {contador} cédulas de R$ {cédula}')
        if cédula == 50:
           cédula = 20
        elif cédula == 20:
           cédula = 10
        elif cédula == 10:
           cédula = 1
        contador = 0
        
        if total == 0:
            break