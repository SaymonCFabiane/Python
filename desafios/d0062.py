primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
i = 0
q = 10
r = 1
t = 0
while r > 0:
    while i < q:
        print(primeiro_termo, end=' -> ')
        primeiro_termo += razao   
        i += 1
        t += 1
    r = int(input('\nQuer mostrar mais alguns termos? se sim digite quantos se não digite 0: '))
    q = r
    i = 0
print(f'Progressão finalizada com {t} termos mostrados.')
