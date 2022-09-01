print('Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado'
      ' e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, '
      'sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.')


i1= float(input('quantos dias alugados? '))
i2 = float(input('quantos km rodados? '))
pago = (i1*60) + (i2*0.15)
print('O total a pagar é de R${}'.format(pago))
