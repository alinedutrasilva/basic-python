n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
p = n1 ** n2
di = n1 // n2
r = n1 % n2
print('A soma eh {} A Multiplicacao eh {} A Divisao eh {} A Potencia eh {} A Divisao Inteira eh {}'.format(s, m, d, p, di), end='>>>')
print('O resto da divisao eh {}'.format(r))