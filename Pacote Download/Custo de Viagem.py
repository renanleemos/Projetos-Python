d = float(input('Qual a distância em KM da sua viagem? '))
p = 0.5 * d
vl = d * 0.45
if d <= 200:
    print('Você está prestes a fazer uma viagem de {}Km. O preço a pagar é de R$ {:.2f}'.format(d, p))
else:
    print('Você está prestes a fazer uma viagem de {}. O preço a pagar é de R$ {:.2f}.'.format(d, vl))
print('-- FIM --')