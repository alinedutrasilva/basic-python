n = input('Type something: ')
print('The Primitive Type is: ', type(n))
print('Is it only spaces? ', n.isspace())
print('Is it a letter? ', n.isalpha())
print('Is it a number? ', n.isnumeric())
print('Is it a lower letter/number? ', n.islower())
print('Is it an upper letter/number?  ', n.isupper())
print('Is it a decimal number? ', n.isdecimal())
print('Is it a digit? ', n.isdigit())
print('Is it ASCII? ', n.isascii())
print('Is it an identifier? ', n.isidentifier())
print('Is it printable? ', n.isprintable())
print('Is it a title? ', n.istitle())