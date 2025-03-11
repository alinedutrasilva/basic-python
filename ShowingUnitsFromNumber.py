n1 = int(input('Qual o numero de 0 a 9999?'))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10
print("""Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}""".format(u, d, c, m))