import datetime
y = int(input('Qual o ano para analise? (coloque 0 para analisar o modulo atual.) '))
if y == 0:
    y = datetime.date.today().year
if y % 4 == 0 and y % 100 !=0 or y % 400 == 0:
    print('O ano {} eh BISSEXTO.'.format(y))
else:
    print('O ano {} NAO eh BISSEXTO.'.format(y))
