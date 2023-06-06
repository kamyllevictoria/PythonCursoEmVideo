from random import randint
from time import sleep
numbers = []
def number_random():
    for num in range (0,5):
        random_number = randint(0,10)
        print(f'{random_number}', end=' ', flush=True)
        sleep(0.2)
        numbers.append(random_number)
    print(f'\nThe informed numbers were: {numbers}')
    
number_random()


def pair_sum_numbers():
    pair_cont = 0
    pair_sum = 0
    for pair_num in numbers:
        if pair_num % 2 == 0:
            pair_cont += 1
            pair_sum += pair_num
    print(f'There were informed {pair_cont} pair numbers, and the sum between them is {pair_sum}.')

pair_sum_numbers()


def odd_pair_num():
    odd_cont = 0
    odd_sum = 0
    for odd_num in numbers:
        if odd_num % 2 != 0:
            odd_cont += 1
            odd_sum += odd_num
    print(f'There were informed {odd_cont} odd numbers, and the sum between them is {odd_sum}.')

odd_pair_num()

