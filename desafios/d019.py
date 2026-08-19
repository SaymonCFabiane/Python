import random
n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print(f'O escolhido foi {escolhido}!')




'''import random
aluno1 = 'Saymon'
aluno2 = 'Gideão'
aluno3 = 'Rhuan'
aluno4 = 'Matheus'
sorteio = random.choice((aluno1, aluno2, aluno3, aluno4))
print(f'O aluno sorteado foi: {sorteio}')'''
