n= int(input('Informe seu ano de nascimento:'))
print('O seu ano de nascimento é {}.'.format(n))
a= (2023-n)
a1= (2023-n)-18
a2= 18-(2023-n)
if a== 18:
    print('\033[0;30;42m Você deverá se alistar no exército esse ano.\033[m')
elif a>= 18:
    print('\033[0;30;41m Você deverá se alistar no exército esse ano. O atraso dos seus alistamentos antepassados é de {} anos.\033[m'.format(a1))
elif a<= 18:
    print('\033[0;30;46m Você ainda não deverá se alistar no exército. Ainda faltam {} anos para tal ato.\033[m'. format(a2))
