from random import randint
user = int(input("Qual foi o número escolhido pelo computador? "))
num = randint(0, 5)
if user == num:
    print('Parabens! Você venceu!')
else:
    print('Não foi dessa vez. O computador venceu!')
print('O número escolhido pelo computador foi {}!'.format(num))
