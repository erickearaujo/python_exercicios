from math import trunc
print('Crie um programa que leia um número Real '
      'qualquer pelo teclado e mostre na tela a sua porção inteira')

num = float(input('Digite um valor: '))

print('o numero digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))
