
while True:
    n = int(input('Digite um número: '))

    if n < 0:
        break
    
    for t in range(1,11):
        print(f'{n} X {t} = {n * t}')
print('Fim do programa!')