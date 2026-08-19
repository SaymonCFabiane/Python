primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
i = 0
while i < 10:
    print(primeiro_termo, end=' -> ')
    primeiro_termo += razao
    i+= 1
print('Fim')
