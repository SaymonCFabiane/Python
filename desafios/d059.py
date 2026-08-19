p = 0

while p != 5:
    num1 = float(input('Digite o 1º número: '))
    num2 = float(input('Digite o 2º número: '))
    print('\n[1]Somar')
    print('[2]Multiplicar')
    print('[3]Maior')
    print('[4]Novos números')
    print('[5]Sair do programa\n')
    p = int(input('Digite sua escolha: '))

    if p == 1:
        print(f'O resultado da soma é: {num1 +num2}')
    if p == 2:
        print(f'O resultado da multiplicação é: {num1 * num2}')
    if p == 3:
        if num1 > num2:
            print(f'O número {num1} é o maior')
        if num1 < num2:
            print(f'O número {num2} é o maior')
        if num1 == num2:
            print(f'Ambos temos o mesmo valor!')
    else:
        print('Invalido tente novamente!!!')
    

print('Fim do programa!')
