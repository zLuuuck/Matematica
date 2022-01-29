import math

c1 = int(input('Digite o primeiro cateto: '))
c2 = int(input('Digite o segundo cateto: '))

cateto1 = math.pow(c1, 2)
cateto2 = math.pow(c2, 2)
scateto = cateto1 + cateto2
raiz = math.sqrt(scateto)
h = math.ceil(raiz)

print(f'A hipotenusa desse triângulo retângulo é {h}')
print(f'h² = {c1}² + {c2}²')
print(f'h² = {cateto1} + {cateto2}')
print(f'h² = {scateto}')
print(f'h = √{scateto}')
print(f'Assim, chegando ao resultado de {h},', end=' ')
print(f'hipotenusa = {h}, cateto oposto = {c1} e', end=' ')
print(f'cateto adjacente = {c2} !')
