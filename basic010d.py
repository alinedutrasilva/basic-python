d = float(input('Qual a distancia da viagem em km?'))
v1 = d * 0.05
v2 = d * 0.45
if d <= 200:
    print('Para a distancia {:.2f}km o valor da sua viagem sera R${:.2f}'.format(d, v1))
if d > 200:
    print('Para a distancia {:.2f}km o valor da sua viagem sera R${:.2f}'.format(d, v2))

# Alternative:
# d = float(input('Qual a distancia da viagem em km?'))
# preco = d * 0.05 if d <= 200 else distancia * 0.045
# print('Para a distancia {:.2f}, seu valor sera {:.2f}'.format(preco))