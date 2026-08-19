import random as rd

pi = ''
while True:
    num = int(input('Escolha um número: '))
    escolha = str(input('Par oi Impar ? [P/I]: ')).strip().upper()
    a = rd.randint(1,10)
    r = num + a

    if r % 2 == 0:
        pi = 'P'
    else:
        pi = 'I'
    
    if escolha == pi:
        print(f'Parabens você ganhou o computador escolheu {a} e você {num} o resultado foi {r} ou seja um número {pi}!')
    else:
        print(f'Você perdeu o computador escolheu {a} e você {num} o resultado foi {r} ou seja um número {pi}!')
        break
print('Fim do programa!')


