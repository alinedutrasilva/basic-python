f = input('Write a phrase:')
m = f.upper()
c = m.count('A')
l = m.find('A')
r = m.rfind('A')
print("""The letter 'A' shows up {} times in this phrase.
The first time the letter 'A' was in the position {}.
The last time the letter 'A' was in the position {}.""".format(c, l, r))