c= float(input('Informe o valor da casa que desja comprar:'))
s= float(input('Informe o valor do seu salário atual:'))
a= float(input('Informe em quantos anos deseja pagar seu empréstimo, caso confirmado:'))
print('O valor da casa é {}\n O seu salário é de R$ {}\n E o empréstimo será pago em {} anos.'. format (c,s,a))
e=(c/a*12)
if s*0.3>= e:
    print('Será possível realizar o empréstimo.')
else:
    print('Não será possível a realização do empréstimo.')