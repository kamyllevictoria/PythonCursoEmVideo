nome = str(input('Digite seu nome: '))
media = float(input(f'Média do aluno {nome}:'))
print(f'Sua média foi de {media}')
if media >= 6:
    print('Você foi aprovado.')
if media < 6:
    print('Você foi reprovado, estude mais!')