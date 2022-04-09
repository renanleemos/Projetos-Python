n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1 + n2) / 2
if m >= 6:
    print("Parabéns! Você foi aprovado com a nota {:.1f}!".format(m))
else:
    print("Você foi reprovado com a nota {}!".format(m))
