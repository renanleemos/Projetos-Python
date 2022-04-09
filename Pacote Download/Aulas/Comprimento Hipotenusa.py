# Identificando o comprimento da hipotenusa.
'''from math import hypot
co = float(input('Digite o comprimento do Cateto Oposto: '))
ca = float(input('Digite o comprimento do Cateto Adjacente: '))
h = hypot(co, ca)
print('O comprimento da Hipotenusa é igual a {:.2f}.'.format(h))'''
# ou
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))