print('Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar')
i1 = float(input('Quanto de dinheiro você tem na carteira'))
i2 = float(i1/3.27)
print('com {}R$ Reais é possivel comprar US${:.2f} Dólares'.format(i1, i2))