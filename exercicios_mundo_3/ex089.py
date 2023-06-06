# informações= []
# dados= []
# while True:
#     nome= str(input('Informe o seu nome:'))
#     n1= float(input('Digite sua primeira nota:'))
#     n2= float(input('Digite sua segunda nota:'))
#     media= (n1+n2)/2
#     dados.append(nome)
#     dados.append(n1)
#     dados.append(n2)
#     dados.append(media)
#     informações.append(dados[:])
#     dados.clear()
#     pergunta= str(input('Deseja ter acesso ao boletim geral?[S/N]')).upper().strip()
#     while pergunta not in 'SsNn':
#         pergunta= str(input('Opção inválida, tente novamente!'))
#     if pergunta in 'Ss':
#             break
# for m in informações:
#     print(f'{m[0]} tem média de {m[3]}')



valores = []
dados = []
soma_v = 0
for c in range (0,3):
    codigo = int(input('Informe o código da cidade: '))
    veiculos = int(input('Informe o número de veículos circulantes: '))
    acidentes = int(input('Informe o número de acidentes por ano: '))
    dados = [codigo, veiculos, acidentes] 
    valores.append(dados)
    soma_v += veiculos

media= (soma_v)/len(valores)  
maior = menor = valores[0][2] 

for c in valores:
        if c[2] > maior:
            maior = c[2]
        if c[2] < menor:
            menor = c[2]
print(f'A média do número de veiculos entre as cidades mencionadas é de {media}.')
print(f'O maior número de acidentes é {maior}.')
print(f'O menor número de acidentes é de {menor}.')
        