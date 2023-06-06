valores= []
while True:
    num= (int(input('Digite um número:')))
    if num not in valores:
       valores.append(num)
    resposta= str(input('Deseja continuar? [S/N]')).upper().strip()
    while resposta not in 'sSnN':
        resposta = str(input('Operação não disponível. Digite uma resposta válida!: '))
    if resposta in 'Nn':
        break
valores.sort()
print(f'O valor informado é de {valores}.')
    