import math
print('Faça um programa que leia um ângulo qualquer e mostre '
      'na tela o valor do seno,cosseno e a tangente desse ângulo')

angu = float(input('Digite o ângulo que você deseja'))
seno = math.sin(math.radians(angu))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angu,seno))
cosseno = math.cos(math.radians(angu))
print('Oâ ngulo de {} tem o COSSENO de {:.2f}'.format(angu,cosseno))
tangente = math.tan(math.radians(angu))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angu,tangente))


