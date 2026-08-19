'''
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o seu sexo: ')).upper()
    if sexo != 'M' and sexo != 'F':
        print('Invalido, escreve direito aberração!!')

if sexo == 'M':
    sexo = 'Masculino'
elif sexo == 'F':
    sexo = 'Feminino'
print(f'Seu sexo é o sexo {sexo}')
'''


sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFm':
    sexo = str(input('Dados invalidos. Por favor informe o seu sexo: ')).strip().upper() [0]

if sexo == 'M':
    sexo = 'Masculino'
elif sexo == 'F':
    sexo = 'Feminino'
print(f'Sexo {sexo} registrado com sucesso')
