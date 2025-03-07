n = input('Type something: ')
print('The Primitive Type is: {} ' "\n"
      'Is it only spaces? {} ' "\n"
      'Is it a letter? {} ' "\n"
      'Is it a number? {} ' "\n"
      'Is it a lower letter/number? {} ' "\n"
      'Is it an upper letter/number? {} ' "\n"
      'Is it a decimal number? {} ' "\n"
      'Is it a digit? {} ' "\n"
      'Is it ASCII? {} ' "\n"
      'Is it an identifier? {} ' "\n"
      'Is it printable? {} ' "\n"
      'Is it a Capitalized? {} ' "\n"
      'Is it alphanumeric? {} ' "\n"
      .format(type(n), n.isspace(), n.isalpha(),
      n.isnumeric(), n.islower(), n.isupper(), n.isdecimal(),
      n.isdigit(), n.isascii(), n.isidentifier(), n.isprintable(),
      n.istitle(), n.isalnum()))