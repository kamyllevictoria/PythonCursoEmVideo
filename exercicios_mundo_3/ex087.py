matriz= [0,0,0],[0,0,0],[0,0,0]
somapar= 0
somat= 0
maior= 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]= int(input(f'Digite um número para a posição [{l},{c}]:'))
        if matriz[l][c]%2 == 0:
            somapar += matriz[l][c]
        if c == 1:
            somat += matriz[l][c]   
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]', end='')
    print()
print(f'A soma dos valores pares digitados é de {somapar}')
print(f'A soma dos valores da segunda coluna é dado por {somat}')
for l in range (0,3):
    if l == 0:
        maior= matriz[l][c]
    elif matriz[l][c] > maior:
        maior= matriz[l][c]
print(f'O maior valor da terceira linha é de {maior}')

