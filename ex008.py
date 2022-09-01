print('Escreva um rpograma que leia um valor em metros e o exiba convertido em centimetros e milimetros')

i1 = float(input('Digite o valor em metros'))
i2 = float(i1*100)
i3 = float(i1*1000)

print('O numero digitado foi {} esse número '
      'convertido para centimetros da o valor de {:.0f} Centimetros, e {:.0f} milimetros'.format(i1, i2, i3))
