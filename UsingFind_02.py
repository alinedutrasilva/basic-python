name = str(input('What is your full name?')).strip()
m = name.upper()
print("""Your full name is: {}.
Does your name has SMITH?""".format(name), 'SMITH' in m)