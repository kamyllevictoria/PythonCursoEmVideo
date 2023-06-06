frase= str(input('Digite uma expressão com parentesês:'))
while True:
    if frase.count('(') != frase.count(')'):
        print('Opção inválida, tente novamente!')
        frase= str(input('Digite uma expressão com parênteses:'))
    else:
        break
print('Fim do programa.')
   
    
