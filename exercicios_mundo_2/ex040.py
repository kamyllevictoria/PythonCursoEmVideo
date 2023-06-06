n1= int(input('Digite sua primeira nota:'))
n2= int(input('Digite sua segunda nota:'))
m= (n1+n2)/2
if m== 7:
    print('\033[0;30;46m Você foi aprovado!\033[m')
elif m>= 7:
    print('\033[0;30;42m Meus parabéns, você foi aprovado!\033[m')
elif m<= 7:
    print('\033[0;30;41m Você não foi aprovado, estude mais!\033[m')
