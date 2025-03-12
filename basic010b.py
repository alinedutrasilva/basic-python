v = float(input('Qual a velocidade em km/h do carro? '))
m = (v-80) * 7
if v > 80:
    print('Voce foi multado!!')
    print('Sua multa eh de R${:.2f}'.format(m))
else:
    (print('Parabens!! Voce estava dentro da velocidade, nao ha multas a serem aplicadas.'))