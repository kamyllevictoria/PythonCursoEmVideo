somaidade= 0
mediaidade= 0
maioridadehomem= 0
nomevelho= ''
totalmulher= 0
for pessoa in range(1,5):
    print('----{} pessoa----'.format(pessoa))
    nome= str(input('Digite seu nome:'))
    idade= int(input('Digite sua idade:'))
    sexo= str(input('Sexo: [M/F]:')).strip()
    somaidade= somaidade+ idade
    if pessoa== 1 and sexo== 'Mm':
        maioridadehomem= maioridadehomem+ 1
        nomevelho= nome
    if sexo in 'Mn' and idade> maioridadehomem:
        maioridadehomem= idade
        nomevelho= nome   
    if sexo in 'Ff' and idade< 20:
        totalmulher= totalmulher+1
            
mediaidade= somaidade/4
print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('A idade do homem mais velho é de {} anos e seu nome é {}.'.format(idade, nomevelho))
print('Ao todo, temos {} mulheres com menos de 20 anos.'.format(totalmulher))    