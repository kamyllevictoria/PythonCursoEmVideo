p= float(input('Iforme seu peso em kg:'))
a= float(input('Informe sua altura em m:'))
imc= p/(a**2)
print('Seu peso é {}kg e sua altura é {}m.'.format(p,a))
print('seu imc é {}.'. format(imc))
if imc<=18.5:
    print('Você está abaixo do peso.')
elif 18.5<=imc<=25:
    print('Você está no peso ideal.') 
elif 25>=imc>=30:
    print('Você está com sobrepeso.')
elif 30>=imc>=40:
    print('Você está com obesidade mórbida.')