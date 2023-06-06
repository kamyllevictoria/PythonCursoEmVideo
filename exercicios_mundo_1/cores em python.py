n1= int(input('Digite sua primeira nota:'))
n2=int(input('Digite sua segunda nota:'))
m= (n1+n2)/2
if m>= 6:
    print('\033[0;30;42m Meus parabéns!\033[m')
else: 
    print('\033[0;30;41m Estude mais!\033[m')