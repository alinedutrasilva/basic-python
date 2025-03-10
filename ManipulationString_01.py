name = str(input('What is your full name? '))
m = name.upper()
n = name.lower()
q = name.split()
l = len(name)
pname = len(q[1])
print("""You Full name with upper letters is: {} 
You Full name with lower letters is: {}
Your full name contains {} letter without spaces
Your first name contains {} letters.""".format(m, n, l, pname))