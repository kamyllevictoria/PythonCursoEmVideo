try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print(f'Tivemos um problema com os tipos de dados que você informou, tente novamente mais tarde!')
except ZeroDivisionError:
    print('Não é possível realizar uma operação com o denominador igual a zero.')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados.')
except Exception as erro:
    print(f'O erro encontrado foi {erro}.')
else:
    print(f'O resultado é {r:.2f}.')
finally:
    print('Volte sempre, muito obrigado!')