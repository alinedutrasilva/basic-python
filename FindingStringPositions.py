name = str(input('What is your full name?')).strip()
s = name.split()
p = s[0]
u = s[-1]
print("""Your full name is: {}.
Your first name is: {}.
Your last name is: {}.""".format(name, p, u))

# Alternative 1:
# name = str(input('What is your full name?')).strip()
# s = name.split()
# print("""Your full name is: {}.
# Your first name is: {}.
# Your last name is: {}.""".format(name, name[0], name[len(name)-1]))
