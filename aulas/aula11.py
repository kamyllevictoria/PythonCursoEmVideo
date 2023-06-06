# pessoas = {'nome': 'Ana', 'sexo': 'F', 'idade': 18}
# pessoas['nome'] ='Leandro'
# del pessoas['sexo']
# for k, v in pessoas.items():
#     print(f'O {k} é {v}')

# brasil = []
# estado = {'uf' : 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'São Paulo', 'siga' : 'SP'}
# brasil.append(estado)
# print(brasil[0]['uf'])


estado = dict()
brasil = list()
for c in range (0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado ['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
for e in brasil:
    for k,v in e.items():
        print(f'O campo {k} é {v}.')