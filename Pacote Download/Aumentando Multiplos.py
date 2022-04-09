sal = float(input('Qual o seu salário? '))
au = (sal * 10) / 100
au2 = (sal * 15) / 100
ns = sal + au
ns2 = sal + au2
if sal > 1250:
    sal = au
    print('O seu salário com aumento de 10% é de R$ {}'.format(ns))
else:
    sal = au2
    print('O seu salário com aumento de 15% é de R$ {}'.format(ns2))
print('-- FIM --')



