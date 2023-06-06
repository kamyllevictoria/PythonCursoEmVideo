primeiro= int(input('Primeiro termo:'))
razão= int(input('Razão da pa:'))
termo= primeiro
contador= 1
termoamais= 10
total= 0
while termoamais != 0:
    total= total+ termoamais
    while contador<= total:
        print('{}'.format(termo), end= '-')
        termo= termo+ razão
        contador= contador+ 1
    print('PAUSA')
    termoamais= int(input('Quantos termos você ainda quer mostrar?'))
print('Progressão realizada com {} termos mostrados.'.format(total))