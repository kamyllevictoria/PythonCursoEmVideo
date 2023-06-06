divida = float(input('Digite o valor da sua dívida: '))
while divida != -1:
    parcela= int(input('Digite o número de parcelas: '))
    if parcela == 1:
        juros = 0
    if parcela == 3:
        juros = 0.10
    if parcela == 0.06:
        juros = 0.15
    else:
        juros = 0.20
    vjuros= divida * juros
    vparcela= (divida + vjuros)/parcela
    print(f'Divida: {divida:.2f}')
    print(f'Quantidade de parcelas: {parcela}')
    print(f'Parcelas sem uros: {vjuros:.2f}')
    print(f'Parcelas com juros: {vparcela:.2f}') 
