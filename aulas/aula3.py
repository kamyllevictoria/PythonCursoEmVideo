#
n1= float(input('Digite sua primeira nota:'))
n2= float(input("Digite sua segunda nota:"))
m= (n1+n2)/2
print('A sua média é de {:.2f}'.format(m))

print('PARABENS' if m>= 6 else 'ESTUDE MAIS') (forma simplificada)

if m>= 6.0:
    print('Parabéns pelo seu desempenho!')
else:
    print('Seu desempenho não foi tão bom, tente novamente nas próximas recuperações.')

    