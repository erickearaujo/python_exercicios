from math import hypot

print('Faça um programa que leia o comprimento do cateto oposto '
      'e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa')

co = float(input('Digite o comprimento do cateto oposto'))
ca = float(input('Digite o comprimento do cateto adjacente '))
hi = math.hypot(co,ca)

print('A Hipotenusa vai medir {:.2f}'.format(hi))