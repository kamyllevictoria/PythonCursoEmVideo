s= int(input('Informe o seu atual salário:'))
print ('O salário informado é de {}.' .format(s))
s1= s+(0.1*s)
s2= s+(0.15*s)
if s>= 1250:
    print('O aumento salarial foi de {}.'. format(s1))
else: 
    print('O aumento salarial foi de {}.'. format(s2)) 