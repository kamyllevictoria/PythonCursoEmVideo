from random import randint
n = randint(0,10), randint(0,10), randint(0,10), randint(0,10)
print(f'Os números informados foram {n}')
print(f'O número 9 apareceu {n.count(9)} vez(es)')
if 3 in n:
    print(f'O número 3 apareceu na posição {n.index(3)+1}')
else:
    print(f'O valor 3 não foi localizado em nenhuma posição')
for n1 in n:
    if n % 2 == 0:
        print (n, end='')

    
    
