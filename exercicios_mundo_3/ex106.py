c = ('\033[m', #branco [0]
     '\033[0;30;41m', #vermelho [1]
     '\033[0;30;42m', # verde [2]
     '\033[0;30;43m', #amarelo [3]
     '\033[0;30;44m', #roxo [4]
     '\033[0;30;45m', #rosa [5]
     '\033[0;30;46m' #nao sei [6]
     '\033[7;30m' #cinza [7]
     );


def ajuda(com):
    titulo(f'Acessando o manual do comando: \'{com}\'', 5)
    print(c[0], end='')
    help(com)
    print(c[0], end='')

def titulo (msg, cor=0):
    tamanho = len(msg) + 4
    print(c[cor], end='')
    print('-'*tamanho)
    print(f'  {msg}  ')
    print('-'*tamanho)
    print(c[0], end='')
    
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP',3)
    comando = str(input('Função ou bibioteca: '))
    if comando.upper() == 'FIM':
        break 
    else:
        ajuda(comando)
titulo('Até mais!',6)