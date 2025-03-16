c = float(input('Qual o valor da casa em R$?'))
s = float(input('Qual o seu salario em R$?'))
a = int(input('Quantos anos deseja pagar o emprestimo?'))
p = c / (a * 12) # Pois quero saber quanto sera a prestacao MENSAL.
m = s * 0.30
if p <= m:
    print('Sua prestacao foi APROVADA e sera no valor mensal de R${}'.format(p))
else:
    print('Sua prestacao foi NEGADA!')