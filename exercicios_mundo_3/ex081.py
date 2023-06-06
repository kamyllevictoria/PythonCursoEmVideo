valores= []
while True:
    num= int(input('Digite um número:'))
    if num not in valores:
        valores.append(num)  
    pergunta= str(input('Deseja continuar?[S/N]')).upper().strip()
    while pergunta not in 'SsNn':
        pergunta= str(input('Opção inválida, tente novamente!'))
    if pergunta in 'Nn':
        break
print(f'O total de números digitados foi de {len(valores)}.')   
valores.sort(reverse=True)     
print(f'A lista de valores na ordem decrescente é dada por {valores}')   
p = valores.index(5)
if 5 in valores:
    print(f'O número 5 está presente na lista e ocupa a posição {p+1}.')
else:
    print(f'O número 5 não está presente na lista.')
