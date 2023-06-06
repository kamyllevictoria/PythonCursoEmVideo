def fatorial(num=1):
    n = 1
    for cont in range (num,0,-1):
        n *= cont
    return n

answare = fatorial(6)
print(answare)
f1 = int(input('Now, its your time! Inform a number to see yor factorial: '))
print(f'The factorial of the number {f1} is {fatorial(f1)}')
