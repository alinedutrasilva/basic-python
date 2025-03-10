import math
a = float(input('What is the angle? '))
s = math.sin((math.radians(a)))
c = math.cos((math.radians(a)))
t = math.tan((math.radians(a)))
print('The angle {} has the sine {:.3f} o cosine {:.3f} and tangent {:.3f}.'.format(a, s, c, t))

# Alternative 1:
# import math
# a = float(input('What is the angle? '))
# print('The angle {} has the sine {:.3f} o cosine {:.3f} and tangent {:.3f}.'.format(math.sin(math.radians(a), math.sin(math.radians(s), math.sin(math.radians(c), math.sin(math.radians(t)))

# Alternative 2:
# from math import radians, sin, cos, tan
# s = sin((radians(a)))
# c = cos((radians(a)))
# t = tan((radians(a)))
# print('The angle {} has the sine {:.3f} o cosine {:.3f} and tangent {:.3f}.'.format(a, s, c, t))