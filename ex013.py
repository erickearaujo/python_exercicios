print('Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário com 15% de desconto')

i1= float(input('Digite o valor do salário: '))
i2= float(i1*(15/100))
i3 = float(i1+i2)

print('O salário do funcionário era de R${} Reais '
      'com o aumento de 15% ficou R${} Reais'.format(i1,i3))