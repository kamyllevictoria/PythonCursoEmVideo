import math
a=float(input('Digite o valor de um ângulo:'))
seno= math.sin(math.radians(a))
cosseno= math.cos(math.radians(a))
tangente= math.tan(math.radians(a))
print('O ângulo {} possui:\n seno de {}\n cosseno {}\n tangente {}'.format(a, seno, cosseno, tangente))

