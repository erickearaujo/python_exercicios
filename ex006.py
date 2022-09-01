print('Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada')

n1 = float(input('Digite um número'))
dob = (n1+n1)
tripl =(n1*3)
rai = (n1**(1/2))

print('O número digitado foi {} o dobro desse núemro é {} '
      'e o triplo é {} sua raiz quadrada é {:.2f}'.format(n1,dob, tripl, rai))