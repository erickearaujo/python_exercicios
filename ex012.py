print('Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.')

i1= float(input ('digite o preço do produto'))
i2 = float(i1 *(5/100))
i3 = (i1-i2)

print('O preço do produto é {} com 5% de desconto '
      'fica {} Reais  pois teve  {} de desconto'.format(i1, i3, i2))