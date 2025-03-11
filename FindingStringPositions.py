name = str(input('What is your full name?')).strip()
s = name.split()
p = s[0]
u = s[-1]
print("""Your full name is: {}.
Your first name is: {}.
Your last name is: {}.""".format(name, p, u))