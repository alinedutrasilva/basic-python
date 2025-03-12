n1 = float(input('Qual o primeiro numero?'))
n2 = float(input('Qual o segundo numero?'))
n3 = float(input('Qual o terceiro numero?'))
if n3<n1>n2:
    print('O numero {} eh o maior.'.format(n1))
if n1<n2>n3:
    print('O numero {} eh o maior.'.format(n2))
if n2<n3>n1:
    print('O numero {} eh o maior.'.format(n3))
if n3>n1<n2:
    print('O numero {} eh o menor.'.format(n1))
if n1>n2<n3:
    print('O numero {} eh o menor.'.format(n2))
if n2>n3<n1:
    print('O numero {} eh o menor.'.format(n3))

# Alternative:
# n1 = float(input('Qual o primeiro numero?'))
# n2 = float(input('Qual o segundo numero?'))
# n3 = float(input('Qual o terceiro numero?'))
# menor = n1
# if n2<n1 and n2<n3
#   menor = n2
# if n3<n1 and n3<n2
#   menor = n3
# maior = n1
# if n2>n1 and n2>n3
#    maior = n2
# if n3>n1 and n3>n2
#    maior = n3
# print('O numero menor eh {}'.format(menor))
# print('O numero maior eh {}'.format(maior))