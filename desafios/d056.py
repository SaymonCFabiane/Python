soma_idade = 0
maioridade_homem = 0
nome_velho = ''
mulher_idade = 0

for p in range(1, 5):
    print(f'---- {p} PESSOA ----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma_idade += idade
    if p == 1 and sexo in 'Mm':
        maioridade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maioridade_homem:
        maioridade_homem = idade
        nome_velho = nome
        
    if sexo in 'Ff' and idade < 20:
        mulher_idade += 1

print(f'A média de idade do grupo é de {soma_idade / p} anos.')
print(f'O homem mais velho é {nome_velho} e tem {maioridade_homem} anos.')
print(f'Tem {mulher_idade} mulheres com menos de 20 anos')
