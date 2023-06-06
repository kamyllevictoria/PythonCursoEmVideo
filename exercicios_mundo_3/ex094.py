dados = []
soma = media = 0
while True:
    pessoas = {}
    pessoas['Nome'] = str(input('Digite seu nome: '))
    
    pessoas['Sexo'] = str(input('Digite seu sexo: [F/M]')).upper().strip()[0]
    while pessoas['Sexo'] not in 'FfMm':
        pessoas['Sexo']= str(input('Opção inválida, tente novamente! [F/M]')).upper().strip()[0]
        
    pessoas['Idade'] = int(input('Digite sua idade: '))
    soma += pessoas['Idade']
    dados.append(pessoas.copy())
    media = soma/ len(dados)
    
    pergunta = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    while pergunta not in 'SsNn':
        pergunta= str(input('Opção inválida, tente novamente! [S/N]')).upper().strip()[0]
    if pergunta in 'Nn':
        break  
    
# print(dados)
print(f'A média das idades é de {media:.2f} anos.')
print(f'O número de pessoas que participaram da pesquisa foi de {len(dados)}.')
print(f'As mulheres que participaram da pesquisa foram:', end=' ')
for m in dados:
    if m['Sexo'] in 'Ff':
        print(f'{m["Nome"]}', end=' ')
print()

