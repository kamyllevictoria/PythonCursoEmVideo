def line():
    print('-'*30)
    
def line_adaptable (text):
    size = len(text)
    print('-'*size)
    print(text)
    print('-'*size)
    
line_adaptable('Pyhton Functions.')
line()
print('Now, its yor time!')
line()
word = str(input('Inform a phase, please! '))
line()
line_adaptable(word)
