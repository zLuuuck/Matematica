preço = float(input('Digite o preço do produto: R$'))
des = float(input('Digite o a % do desconto: '))
novo = preço - (preço * des / 100)
totaldes = novo - preço

print(f'O preço é R${preço}, com um desconto de {des}%, fica R${novo}.')
print(f'O desconto é de {totaldes}')
