# a = int(input('Inform the start of sequence: '))
# b = int(input('Inform the end of sequence: '))
# c = int(input('Inform the pass of sequence: '))
# for contagem in range (a,b,c):
#     print(contagem)

def line():
    print('-'*30)
    
def contagem (a,b,c):
    print(f'Counting from {a} to {b}, {c} by {c}:')
    if b < 0:
        p *= -1
    if b == 0:
        p = 1
    if a < b:
        cont = a
        while cont <= b:
            print(f'{cont}', end=' ')
            cont += c
        print('End.')
    else:
        cont = a
        while cont >= b:
            print(f'{cont}', end=' ')
            cont -= c
        print('End.')
            
line()
contagem (1,10,1)
line()
contagem(1,10,2)
line()
contagem(10,0,2)
line()
print('Now, its your time!')
a = int(input('Inform the start of sequence: '))
b = int(input('Inform the end of sequence: '))
c = int(input('Inform the pass of sequence: '))
contagem(a,b,c)
line()