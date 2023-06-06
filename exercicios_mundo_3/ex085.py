# valores= [[], []]
# for v in range (1,9):
#     n= int(input(f'Digite o {v}º número:'))
#     if n%2 == 0:
#         valores[0].append(n)
#     else:
#         valores[1].append(n)
# print(valores)
# valores[0].sort()
# valores[1].sort()
# print(f'Os números pares são dados por: {valores[0]}')
# print(f'Os números ímpares são dados por: {valores[1]}')


pessoas= []
medida= [[],[]]
massa= [[],[]]

while True:
    cadastro= str(input('Digite sua matrícula: '))
    pessoas.append(cadastro)
    altura= int(input('Digite sua altura em cm: '))
    if altura > 200:
        medida[1].append(altura)
    else: 
        medida[0].append(altura)
    peso= int(input('Digite o seu peso: '))
    if peso > 150:
        massa[1].append(peso)
    else:
        massa[0].append(peso)
    pergunta = str(input('Deseja continuar a operação? [S/N]')).upper().strip()
    while pergunta not in 'SsNn':
        pergunta = str(input('Opção inválida, tente novamente! [S/N]')).upper().strip()
        if pergunta in 'Nn':
            break 
    print('Fim do programa.')
    print(massa)
    print(medida)
        