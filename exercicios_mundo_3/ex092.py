from datetime import datetime
dados = dict()
dados ['Nome'] = str(input('Digite seu nome: '))
nascimento = int(input('Digite seu ano de nascimento: '))

dados ['Idade'] = datetime.now().year - nascimento

dados ['Carteira'] = int(input('Digite o número da sua carteira de trabalho: '))
if dados ['Carteira']  != 0:
    dados ['Contratado_ano'] = int(input('Qual foi o seu ano de contratação?: '))
    dados ['Salario'] = float(input('Qual foi seu primeiro salário em reais?:'))
    dados ['Aposentadoria'] = ((dados['Contratado_ano'] + 35) - datetime.now().year) + dados['Idade']
else:
    print('Você não possui carteira de trabalho.')
# print(dados)
for k, v in dados.items():
    print(f'{k} possui valor {v}')
