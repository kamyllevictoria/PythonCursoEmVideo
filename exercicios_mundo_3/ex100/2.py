def line():
    print('-'*80)
    
def pair_sum_numbers(*numero):
    pair_cont = 0
    pair_sum = 0
    for p in numero:
        if p % 2 == 0:
            pair_cont += 1
            pair_sum += p
    line()
    print(f'There were informed {pair_cont} pair numbers, and the sum between them is {pair_sum}.')
    line()
# pair_sum_numbers() #o resultado no final será nulo, pois nao informei nenhum argumento
pair_sum_numbers(3,6,2,8,6,1) #aqui o resultado dos numeros pares será informado, pois eu informei os argumentos
line()
print('Now, its your time to try!')
line()

def get(): #essa funçaõ serve para o usuario informar os numeros que serao armazenados em uma lista, depois essa lista sera aplicada na função dos numeros pares
    num_list = []
    while True:
        num = int(input('Inform a number, please: '))
        line()
        num_list.append(num)
        ask = str(input('Do you want to continue adding more numbers? [Y/N]')).upper().strip()[0]
        while ask not in 'YyNn':
            ask = str(input('ERRO! Try again: [Y/N]')).upper().strip()[0]
        if ask in 'Nn':
            break 
    return num_list
num_list = get() #pega os valores da lista, coloca na função 'transporte' e depois joga na função pricipal
pair_sum_numbers(*num_list)