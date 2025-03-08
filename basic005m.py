km = float(input('How many KM? '))
d = int(input('How many days? '))
p = (d * 60) + (km * 0.15)
print('The total for renting this car is {:.2f}'.format(p))