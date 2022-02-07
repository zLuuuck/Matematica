n = int(input('Digite um número entre 0 a 9999: '))

uni = n // 1 % 10
dez = n // 10 % 10
cen = n // 100 % 10
mil = n // 1000 % 10

print(f'O número digitado foi {n}')
print(f'Unidade = {uni}')
print(f'Dezena = {dez}')
print(f'Centena = {cen}')
print(f'Milhar = {mil}')
