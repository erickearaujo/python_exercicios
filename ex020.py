from random import shuffle
print('O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos'
      'dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada')

a1 = str(input('Digite o nome do primeiro aluno'))
a2 = str(input('Digite o nome do segundo aluno'))
a3 = str(input('Digite o nome do terceiro aluno'))
a4 = str(input('Digite o nome do quarto aluno'))
lista = [a1,a2,a3,a4]
shuffle(lista)

print(' O Aluno escolhido foi {}'.format(lista))