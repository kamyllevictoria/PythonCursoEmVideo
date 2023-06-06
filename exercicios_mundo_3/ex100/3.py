def line():
    print('-'*80)
    
def odd_pair_num(*numero):
    odd_cont = 0
    odd_sum = 0
    for odd_num in numero:
        if odd_num % 2 != 0:
            odd_cont += 1
            odd_sum += odd_num
    line()
    print(f'There were informed {odd_cont} odd numbers, and the sum between them is {odd_sum}.')
    line()
    
odd_pair_num(5,9,6,7,3,0,4)
line()
print('Now, its your time to try!')
line()

def get_odd_numbers():
    num_list = []
    while True:
        num = int(input('Inform a number please: '))
        line()
        num_list.append(num)
        ask = str(input('Do you want to continue adding numbers? [Y/N]')).upper().strip()[0]
        while ask not in 'YyNn':
            ask = str(input('ERROR! Try again! [Y/N]')).upper().strip()[0]
        if ask in 'Nn':
            break 
    return num_list
num_list = get_odd_numbers()
odd_pair_num(*num_list)