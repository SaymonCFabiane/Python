from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será ')
print(lista)




'''
import random
aluno1 = 'Lucas'
aluno2 = 'Ivan'
aluno3 = 'João'
aluno4 = 'Wesley'
sorteio = list ((aluno1, aluno2, aluno3, aluno4))
random.shuffle(sorteio)
print(f'O aluno sorteado foi: {sorteio}')
'''