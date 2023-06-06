def area(wodth, length):
    area_total = wodth * length
    print(f'The total area is {wodth}m x {length}m = {area_total}m².')
    
area(8,6)

print('Now, its your time: ')
wodth = float(input('Inform the land width (m): '))
length = float(input('Inform the land length (m): '))
area(wodth, length)