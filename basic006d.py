import math
a = float(input('What is the angle? '))
s = math.sin(a)
c = math.cos(a)
t = math.tan(a)
print('The angle {} has the sine {:.3f} o cosine {:.3f} and tangent {:.3f}.'.format(a, s, c, t))