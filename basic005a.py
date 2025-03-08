n1 = int(input('Type a number: '))
n2 = int(input('Type another number: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
p = n1 ** n2
di = n1 // n2
r = n1 % n2
print('The Sum is {} The Multiplication is {} The Division is {} A Potencia eh {} A Divisao Inteira eh {}'.format(s, m, d, p, di), end='>>>')
print('O resto da divisao eh {}'.format(r))