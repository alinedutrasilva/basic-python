f = str(input('Write a phrase:')).strip()
m = f.upper()
c = m.count('A')
l = m.find('A')
r = m.rfind('A')
print("""The letter 'A' shows up {} times in this phrase.
The first time the letter 'A' was in the position {}.
The last time the letter 'A' was in the position {}.""".format(c, l, r))

# Alternative 1:
# f = str(input('Write a phrase:')).strip().upper()
# c = f.count('A')
# l = f.find('A')
# r = f.rfind('A')
# print("""The letter 'A' shows up {} times in this phrase.
# The first time the letter 'A' was in the position {}.
# The last time the letter 'A' was in the position {}.""".format(c, l, r))

# Alternative 2:
# f = str(input('Write a phrase:')).strip().upper()
# c = f.count('A')
# l = f.find('A') <---- So the counting would not mention/count as "posicao 0", which would confuse final user.
# r = f.rfind('A') <---- So the counting would not mention/count as "posicao 0", which would confuse final user.
# print("""The letter 'A' shows up {} times in this phrase.
# The first time the letter 'A' was in the position {}.
# The last time the letter 'A' was in the position {}.""".format(c, l, r))