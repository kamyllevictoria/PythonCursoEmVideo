frase= str(input('Digite uma frase para ver se é um palíndromo!'))
palavras= frase.split()
junto= ''.join(palavras)
inverso= ''
for letra in range (len(junto)-1,-1,-1):
    inverso= inverso+ junto[letra]
print(junto,inverso)
if junto== inverso:
    print('Temos um palíndromo! ')
else:
    print('A frase não é um palíndromo.')