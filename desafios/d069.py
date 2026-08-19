c18 = 0
hc = 0
mi = 0

while True:
    print('\n')
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
    if idade > 18:
        c18 +=1
    if sexo == 'M':
        hc += 1
    if sexo == 'F' and idade < 20:
        mi += 1
    continuar = str(input('Deseja continuar[S/N]: ')).strip().upper()
    if continuar != 'S':
        break


print('\n')
print(f'A) {c18} tem mais de 18 anos!')
print(f'B) {hc} homens foram cadastrados!')
print(f'C) {mi} mulheres tem mais de 20 anos!\n')
