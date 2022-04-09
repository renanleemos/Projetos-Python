# Identificando o seno, cosseno e o tangente de um angulo.
from math import sin, cos, tan
angulo = float(input('Qual é o ângulo? '))
seno = math.sin(math.radians(angulo))
print('O angulo {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O angulo {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O angulo {} tem o TANGENTE de {:.2f}'.format(angulo, tangente))