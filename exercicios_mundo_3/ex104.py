def inteiro(num):
    valor = 0
    while True:
        ok = False
        n = input(num)
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO. Digite um número inteiro válido!\033[m')
        if ok:
            break 
    return valor
n = inteiro('Digite um número: ')
print(f'Você informou o número {n}.')


