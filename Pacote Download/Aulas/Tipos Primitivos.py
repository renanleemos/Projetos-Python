# Como eu fiz
# p1 = type(input('Digite algo: '))
# print('O tipo primitivo desse valor é {}'.format(p1))
# print('Tem espaços?', bool())
# print('É um número?', bool())
# print('É alfabético? ', bool('p1'))
# print('É alfanumérico? ', bool('p1'))
# print('Está em maiúscula? ', bool())
# print('Está em minúsculas? ', bool())
# print('Está capitalizada? ', bool('p1'))
# Como eu fiz 

# Como o Guanabara fez.
p1 = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(p1))
print('Só Tem espaços? ', p1.isspace())
print('É alfabético? ', p1.isalpha())
print('É alfanumérico? ', p1.isalnum())
print('Está em maiúscula? ', p1.isupper())
print('Está em minúscula? ', p1.islower())
print('Está capitalizada? ', p1.istitle())
# Como o Guanabara fez.