def notas (*n, situação=False):
    """Função para analisar notas dos alunos e retornar:
    -A maior nota
    -A menor nota
    -Calcular a média e mostrar a situação estudantil do aluno, com base no seu desempenho escolar
    -Usamos o return para retornar os valores contidos no dicionário.
    """

    dicionário = {}
    cont = len(n)
    dicionário['Quantidade'] = cont
    dicionário['Maior nota'] = max(n)
    dicionário['Menor nota'] = min(n)
    soma = sum(n)
    dicionário['Média'] = soma/cont
    return dicionário

numeros = []
while True:
    numero = float(input('Informe um número: '))
    numeros.append(numero)
    pergunta = str(input('Deseja adicionar mais números? [S/N]')).upper().strip()[0]
    while pergunta not in 'SsNn':
        pergunta = str(input('ERRO! Tente novamente! [S/N]')).upper().strip()[0]
    if pergunta in 'Nn':
        break 
resposta = notas(*numeros, situação=True)
print(resposta)