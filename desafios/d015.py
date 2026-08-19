dias = int(input('Digite por quantos dias o carro foi alugado: '))
km = float(input('Digite quantos quilometros foram rodados com o carro: '))
valKm = km * 0.15
valDias = dias * 60
valTotal = valKm + valDias
print(f'O total a pagar é de R${valTotal}')
