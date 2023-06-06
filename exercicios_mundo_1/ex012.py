n1=int(input('Olá, bom dia.Você possui um cupom de 5% de desconto para as próximas compras realizadas em uma rede Cacau Show, para consultar o desconto, informe o valor da compra:'))
desconto= n1*(5/100) 
print('O valor da compra sem o cupom é de {}, porém, com o uso do benefício, o valor total será de {}'. format(n1,n1-(n1*(5/100))))
