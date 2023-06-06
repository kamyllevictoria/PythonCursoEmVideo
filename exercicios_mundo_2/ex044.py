print('Lojas Kamylle.')
p= float(input('Informe o valor do produto a ser pago:'))
print('''Formas de pagamento:
[1] à vista dinheiro/cheque
[2] à vista cartão    
[3] 2x cartão  
[4] 3x cartão''')
opção= int(input('Qual é a sua opção?'))
if opção== 1:
    total= p-(p*0.1)
elif opção== 2:
    total= p-(p*0.05) 
elif opção== 3:
    total= p
    parcela= total/2
    print('Sua compra será parcelada em 2x no cartão no valor de R${}.'.format(parcela))
elif opção== 4:
    total= p+(0.2*p)
    totalparc= int(input('Digite o total de parcelas:')) 
    parcela= total/totalparc
    print('Sua compra será parcelada em {}x de R${} com juros.'.format(totalparc,parcela))
print('Sua compra de R${}, no final, será de R${}.'. format(p, total))

