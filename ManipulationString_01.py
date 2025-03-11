name = str(input('What is your full name?')).strip()
m = name.upper()
n = name.lower()
print("""Your full name in capslock is: {} 
Your full name with capslock off is: {}
Your full name contains {} letters.
Your first name contains {} letters.""".format(m, n, len(name) - name.count(' '), name.find(' ')))

# Alternative 1:
# name = str(input('What is your full name?')).strip()
# m = name.upper()
# n = name.lower()
# d = name.split()
# print("""Your full name in capslock is: {}
# Your full name with capslock off is: {}
# Your full name contains {} letters.""".format(m, n, len(name) - name.count(' '))
# print("""Your first name is {} contains {} letters.""".format(d[0], len(d[0]))