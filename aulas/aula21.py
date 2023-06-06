# def fatorial(num=1):
#     f = 1 
#     for cont in range (num,0,-1):
#         f *= cont
#     return f

# f1 = int(input('Digite um número: '))
# print(f'O fatorial do númeors {f1} é {fatorial(f1)}.')

# f2 = fatorial(6)
# f3 = fatorial(9)
# print(f'Os resultados obtidos foram {f2} e {f3}.')

def par (n=0):
    if n % 2 == 0:
        return True
    else:
        return False
    
num = int(input('Digite um número: '))
print(par(num))