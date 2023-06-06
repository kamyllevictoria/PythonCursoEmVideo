# teste = list()
# teste.append('Lucas')
# teste.append(21)
# pessoas = list()
# pessoas.append(teste[:])
# teste[0] = 'Kamylle'
# teste[1] = 19
# pessoas.append(teste[:])
# print(pessoas)



# pessoas= [['Ana',33], ['João',22], ['Lucas',21], ['Kamylle',19]]
# for nomes in pessoas:
#     print(f' {nomes[0]} possui {nomes[1]} anos de idade')
    
    

pessoas= list()
dado= list()
totalmaior= 0
totalmenor= 0
for c in range (0,3):
    dado.append(str(input('Digite o seu nome: ')))
    dado.append(int(input('Digite a sua idade: ')))
    pessoas.append(dado[:])
    dado.clear()
print(pessoas)
for p in pessoas:
    if p[1]>= 18:
        print(f'{p[0]} é maior de idade')
        totalmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totalmenor += 1
print(f' Temos {totalmaior} pessoas maiores de idade')
sleep(2)
print(f' Temos {totalmenor} pessoas menores de idade.')