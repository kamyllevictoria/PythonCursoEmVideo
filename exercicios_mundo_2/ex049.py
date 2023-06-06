n= int(input('Para saber a tabuada de um número multiplicado até 10, digite um número:'))
print(n*12)
for c in range (1,11): 
    print('{} x {}= {}'. format(n,c,n*c))
