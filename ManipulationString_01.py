name = str(input('What is your full name?')).strip()
m = name.upper()
n = name.lower()
print("""Your full name in capslock is: {} 
Your full name with capslock off is: {}
Your full name contains {} letters.
Your first name contains {} letters.""".format(m, n, len(name) - name.count(' '), name.find(' ')))