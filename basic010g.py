s = float(input('Qual o seu salario atual? R$'))
novo = s + (s * 0.10)
outro = s + (s * 0.15)
if s>1250:
    print('Seu novo salario sera acrescido 10%, sendo valor final {:.2f}.'.format(novo))
if s<=1250:
    print('Seu novo salario sera acrescido 15%, sendo valor final {:.2f}.'.format(outro))

# Alternative:
# s = float(input('Qual o seu salario atual? R$'))
# if s>1250:
#   novo = s + (s * 0.10)
# else:
#   novo = s + (s * 0.15)
# print('Quem ganhava {:.2f} passa a ganhar {}.'.format(salario, novo))