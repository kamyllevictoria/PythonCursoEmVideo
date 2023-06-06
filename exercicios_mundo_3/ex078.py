# valor = []
# for v in range (0,5):
#     valor.append(int(input('Digite um valor:')))
# print(f'Você digitou os valores: {valor}')
# for p,v in enumerate(valor):
#     if v == max(valor):
#         print(f'O maior valor é {v} e está na posição {p}')
#     if v == min(valor):
#         print(f'O menor valor é {v} e sua posição é {p}')
        
import random
lista = []
for c in range (0,9):
    lista.append(random.randint(0,9))
print(f'Os valores presentes na lista são: {lista}.')
for v,m in enumerate(lista):
    if m == max(lista):
        print(f'O maior valor da lista é {m} e sua posição é {v}.')
    if m == min(lista):
        print(f'O menor valor da lista é {m} e sua posição é {v}.')