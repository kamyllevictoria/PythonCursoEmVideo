pessoas= list() 
dados= list()
pesadas= []
leves= []
while True:
    nome= str(input('Digite o seu nome: '))
    peso= float(input('Digite o seu peso em kg: '))
    dados.append(nome)
    dados.append(peso)
    if peso >= 100:
        pesadas.append(dados[:])
    else:
        leves.append(dados[:])
    pessoas.append(dados[:])  
    dados.clear()  
    pergunta= str(input(('Deseja continuar a operação? [S/N]'))).upper().strip()
    while pergunta not in 'SsNn':
        pergunta= str(input('Resposta inválida, tente novamente!'))
    if pergunta in 'Nn':
        break
print(pessoas)
print('Fim do programa.')
print(f'O número de pessoas cadastradas é de: {len(pessoas)}.')
print(f'A listagem com o número de pessoas pesadas é dada por: {pesadas}.')
print(f'A listagem com o número de pessoas leves é dada por: {leves}.')