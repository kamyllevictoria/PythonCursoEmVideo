n= int(input('Digite o seu ano de nascimento:'))
print('O seu ano de nascimento é {}.'. format(n))
ano= 2023-n
if ano<= 9:
    print('Você é um atleta mirim.') 
elif ano<= 14:
    print('Você é um atleta infantil.') 
elif ano<= 19: 
    print('Você é uma atleta júnior.')
elif ano<= 20: 
    print('Você é um atleta sênior.') 
elif ano> 20: 
    print('você é um atleta master.') 