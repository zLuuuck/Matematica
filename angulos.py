import math

an = float(input('Digite o ângulo que você deseja:'))
seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tangente = math.tan(math.radians(an))

print(f'Ângulo: {an} ')
print(f'Ângulo Seno: {seno:.2f} ')
print(f'Ângulo Cosseno: {cosseno:.2f} ')
print(f'Ângulo Tangente: {tangente:.2f} ')
