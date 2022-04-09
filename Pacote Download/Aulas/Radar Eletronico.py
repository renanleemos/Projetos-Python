v = float(input('Qual a velocidade do carro? '))
m = (v - 80) * 7
if v > 80:
    print("MULTADO! Você excedeu o limite permitido de 80Km/h. \nVocê deve pagar uma multa de R$ {:.2f}!".format(m))
print('Tenha um bom dia! Dirija com segurança.')
