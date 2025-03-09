a1 = float(input('What is one side of the wall in meters? '))
a2 = float(input('What is the other side of the wall in meters ? '))
at = a1 * a2
t = at / 2
print('Side 1 is {}m'.format(a1))
print('Side 2 is {}m'.format(a2))
print('The area is {}m2'.format(at))
print('You will need {}liters of paint to paint this whole wall.'.format(t))

# 1 liter of paint = 2m2