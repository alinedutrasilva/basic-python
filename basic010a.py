import random
n1 = int(input('Adivinhe o numero de 0 a 5 escolhido pelo computador: '))
if n1 >5:
    print('Numero tem de ser entre 0 a 5.')
if n1 <0:
    print('Numero tem de ser entre 0 a 5.')
n2 = int(0)
n3 = int(1)
n4 = int(2)
n5 = int(3)
n6 = int(4)
n7 = int(5)
lista = [n2, n3, n4, n5, n6, n7]
e = random.choice(lista)
if n1==e:
    print('Parabens voce acertou!!')
else:
    print('Voce errou!')

# Alternative 1:
# from random import randint
# from time import sleep
# computador = radint(0, 5)
# print('Vou tentar pensar num numero entre 0 e 5. Tente adivinhar.')
# print('-=-'*20)
# jogador = int(input('Em que numero eu pensei?'))
# print('PROCESSING...')
# sleep(2)
# if jogador==computador:
#   print('Parabens voce acertou!!')
# else:
#   print('Voce errou!')
#   print('Eu pensei no numero {}'.format(computador))