frase = str(input('Digite uma frase qualquer: ').upper())
print(f'A letra "A" aparece {frase.count('A')}')
print(f'A letra "A" aparece na primeira vez na posição {frase.find('A') + 1}')
print(f'A letra "A" aparece na ultima vez na posição {frase.rfind('A') + 1}')
