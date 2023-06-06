nome= str(input('Digite o seu nome:'))
sexo= str(input('Informe o seu sexo: [F/M]')).upper()
while sexo not in 'F/M':
    sexo= str(input('Dados inválidos, por favor, informe novamente seus dados.')).upper()
print('Olá, {}, seu sexo {} foi registrado com sucesso!'.format(nome, sexo))     