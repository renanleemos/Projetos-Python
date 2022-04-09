n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
max = n1
if n2 > max:
    max = n2
if n3 > max:
    max = n3
print('O maior número é: {}.'.format(max))
min = n1
if n2 < min:
    min = n2
if n3 < min:
    min = n3
print('O menor número é: {}.'.format(min))



