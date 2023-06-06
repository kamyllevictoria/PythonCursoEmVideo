soma = 0
contador = 0
t1000 = 0
menor = 0
while True:
    nome = str(input('Nome do produto:'))
    preço = float(input('Digite o preço do produto R$:'))
    xontador = contador + 1
    soma = soma + preço
    if preço > 1000:
        t1000 = t1000 + 1
    if contador == 1:
        menor = preço     
    else:
        if preço < menor:
            menor = preço         
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N]:')).upper().strip()
    if resposta == 'N':
        break 
print('Acabou o programa!')
print(f'O total da compra foi de {soma}')
print(f'Os produtos que custam mais de R$1000.00 é de {t1000}')
print(f'O produto mais barato custa R$ {menor}')