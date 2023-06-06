valores= []
listapar= []
listaimpar= []
while True:
    num= int(input('Digite um número:'))
    valores.append(num)
    if num%2 == 0:
        listapar.append(num)
    else:
        listaimpar.append(num) 
    resposta= str(input('Deseja continuar a operação? [S/N]')).upper().strip()
    while resposta not in 'SsNn':
        resposta= str(input('Resposta inválida! Tente novamente!'))
    if resposta in 'Nn':
        break
print(f'Os elementos da lista principal são: {valores}.')
print(f'Os números ímpares informados são: {listaimpar}.')
print(f'Os números pares informados são: {listapar}.')