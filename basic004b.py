n = input('Type something: ')
print('The Primitive Type is: {} ' 
      'Is it only spaces? {} ' 
      'Is it a letter? {} ' 
      'Is it a number? {} ' 
      'Is it a lower letter/number? {} ' 
      'Is it an upper letter/number? {} '
      'Is it a decimal number? {} '
      'Is it a digit? {} '
      'Is it ASCII? {} '
      'Is it an identifier? {} '
      'Is it printable? {} '
      'Is it a Capitalized? {} '
      'Is it alphanumeric? {} '
      .format(type(n), n.isspace(), n.isalpha(),
      n.isnumeric(), n.islower(), n.isupper(), n.isdecimal(),
      n.isdigit(), n.isascii(), n.isidentifier(), n.isprintable(),
      n.istitle(), n.isalnum()))