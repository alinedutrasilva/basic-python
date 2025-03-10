import random
n1 = str(input('What is the name of the student 1? '))
n2 = str(input('What is the name of the student 2? '))
n3 = str(input('What is the name of the student 3? '))
n4 = str(input('What is the name of the student 4? '))
list = [n1, n2, n3, n4]
random.shuffle(list)
print('The order of the presentation will be: {}'.format(list))

# Alternative 1:
# from random import shuffle
# n1 = str(input('What is the name of the student 1? '))
# n2 = str(input('What is the name of the student 2? '))
# n3 = str(input('What is the name of the student 3? '))
# n4 = str(input('What is the name of the student 4? '))
# list = [n1, n2, n3, n4]
# shuffle(list)
#print('The order of the presentation will be: {}'.format(list))