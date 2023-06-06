def inteiro(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro, por favor, digite um numero inteiro valido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mOperação interrompida pelo usuário.\033[31m')
            return 0
        else:
            return n


def inteiro_virgula(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\n\033Erro, por favor, digite um número real válido!\033[31m')
        except (KeyboardInterrupt):
            print('\033[31mOperação interrompida pelo usuário.\033[31m')
            return 0
        else:
            return n


num1 = inteiro('Digite um valor inteiro: ')
num2 = inteiro_virgula('Digite um valor real : ')
print(f'O valor inteiro informado foi: {num1}, já o valor real informado foi {num2}.')