nome= str(input('Qual é o seu nome?'))
if nome== 'Kamylle':
    print('Que nome bonito!')
elif nome== 'Debora' or nome== 'Lucas' or nome== 'Victoria':
    print('O seu nome é bem popular!')
elif nome== 'João' or nome== 'Pedro' or nome== 'Larissa':
    print('Seu nome é bem legal')
else: 
    print('O seu nome é bem comum!')
print('Tenha um bom dia {}!.'. format(nome))