import math
co = float(input('Type side of right triangle: '))
ca = float(input('Type the the other side of the triangle: '))
h = math.hypot(co, ca)
print('The hypotenuse is {:.3f}'.format(h))

# Alternative 1:
# h = (co ** 2 + ca ** 2) ** (1/2)

# Alternative 2:
# from math import hypot
# co = float(input('Type side of right triangle: '))
# ca = float(input('Type the the other side of the triangle: '))
# h = hypot(co, ca)
# print('The hypotenuse is {:.3f}'.format(h))