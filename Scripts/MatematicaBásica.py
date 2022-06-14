import os
import platform
import math
'''
Tabuada
raiz quadrada
potencia
porcentagens
'''
txtmatB = '''
|￣￣￣￣￣￣ |   O que deseja?
| Programa de|   [1] Tabuada x100
| Matemática |   [2] Raiz quadrada
|   do Z     |   [3] Potencia
| ___________|   [4] Porcentagens
(\__/)||
(•ㅅ•)||
/    づ
'''
txtc = '''
|￣￣￣￣￣￣ |
| Programa de|
| Matemática |
|   do Z     |
| ___________|
(\__/)||
(•ㅅ•)||
/    づ
'''

def limpar():
    sistema = platform.system()
    if sistema == 'Windows':
        os.system('cls')
    elif sistema == 'Linux':
        os.system('clear')

class MatemáticaBásica:
    def Tabuada():
        limpar()
        print(txtc)
        print('Tabuada x100')
        nu = int(input('\nDigite um número: '))
        for c in range(0, 101):
            print(f'{nu} x {c} = {nu * c}')
    
    def Raiz4():
        limpar()
        print(txtc)
        print('Raiz Quadrada')
        nu = int(input('\nDigite um número: '))
        print(f'A raiz quadrada de {nu} é {math.sqrt(nu)}')
        
    def potencia():
        limpar()
        print(txtc)
        print('Potencia')
        nu = int(input('Digite um número: '))
        expoente = int(input('Digite o expoente: '))
        print(f'O {nu} elevado ao {expoente} resulta em {math.pow(nu, expoente)}')
        
                
    def porcentagem():
        limpar()
        print(txtc)
        print('Porcentagem')
        print('Digite o valor ou o preço (se for um preço, utilize (.) invés de virgula (,)\nexemplo: 499.99')
        nu = float(input(': '))
        porcent = float(input('Digite a porcentagem: '))
        porcentagem = nu * porcent / 100
        e = str(input('é um aumento ou um desconto? [a/d] ')).lower()
        while e not in 'ad':
            e = str(input('é um aumento ou um desconto? [a/d] ')).lower()
        if e == 'a':
            total = nu + porcentagem
            print(f'''
O valor digitado foi {nu:.2f}. 
Aumentando {porcent}% desse número. {porcent}% de {nu:.2f} é = a {porcentagem:.2f}.
Aplicando a porcentagem, ele vale {total:.2f}.
Ganhou-se {porcentagem:.2f}.''')
        elif e == 'd':
            total = nu - porcentagem
            print(f'''
O valor digitado foi {nu:.2f}. 
Aumentando {porcent}% desse número. {porcent}% de {nu:.2f} é = a {porcentagem:.2f}.
Aplicando a porcentagem, ele vale {total:.2f}.
Perdeu-se {porcentagem:.2f}.''')

    limpar()
    print(txtmatB)
    opção = input(': ')
    while opção not in '1234':
        opção = input(': ')
    if opção == '1':
        Tabuada()
    elif opção == '2':
        Raiz4()
    elif opção == '3':
        potencia()
    elif opção == '4':
        porcentagem()
