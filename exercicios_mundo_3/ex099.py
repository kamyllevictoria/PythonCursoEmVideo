def big (*num):
    maior = 0
    cont = 0
    print('\nAnalyzing the informed values...')
    for value in num:
        print(f'{value}', end=' ')
        if cont == 0:
            maior = value
        else:
            if value > maior:
                maior = value
        cont += 1 
    print(f'\nThere were informed {cont} numbers, and the biggest is {maior}.')
big(1,4,6,2)
big(9,6,2,8,1)
big(0,7,1)