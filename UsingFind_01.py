city = str(input('What is the name of your city?')).strip()
m = city.upper()
print("""Your city is: {}.
Does it have the word 'Los' within? {}""".format(city, m[:5] == 'SANTO'))

# Alternative 1:
# city = str(input('What is the name of your city?'))
# m = city.upper()
# print("""Your city is: {}.
# Does it have the word 'Los' within? {}""".format(city), 'LOS' in m)