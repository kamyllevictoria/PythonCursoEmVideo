lista = ('Kamylle', 'Lucas', 'Vitoria', 'Anna')
for nomes in lista:
        print(f'Na palavra {nomes} temos as seguintes vogais: ',end='')
        for letras in nomes:
            if letras.lower() in 'aeiou':
                print(f'{letras} ', end='')
        print()
