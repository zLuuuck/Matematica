import os
import platform
import math


def limpar():
    sistema = platform.system()
    if sistema == 'Windows':
        os.system('cls')
    elif sistema == 'Linux':
        os.system('clear')
txt = '''
|￣￣￣￣￣￣ |   O que deseja?
| Programa de|   [1] Pitagoras
| Matemática |   [2] Produtos notáveis
|   do Z     |
| ___________|
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
txtnot = '''
|￣￣￣￣￣￣ |   O que deseja?
| Programa de|   [1] Quadrado da Soma
| Matemática |   [2] Quadrado da Diferença
|   do Z     |   [3] Produto da Soma pela Diferença
| ___________|
(\__/)||
(•ㅅ•)||
/    づ
'''
class MatematicaDiferenciada:
    def Pitagoras():
        limpar()
        print(txtc)
        print('Pitagoras')
        print('Descobrindo um cateto ou a hipotenusa? ')
        opção = str(input('[C/H] ')).upper()
        while opção not in 'CH':
            opção = str(input('[C/H] ')).upper()
        if opção == 'C':
            limpar()
            print(txtc)
            print('Descobrindo um dos Catetos.')
            c = int(input('Digite o cateto: '))
            h = int(input('Digite a hipotenusa: '))
            c1 = math.pow(c, 2)
            h1 = math.pow(h, 2)
            s = h1 - c1
            raiz = math.sqrt(s)
           
            print(f'O Cateto desse triângulo retângulo é {c}')
            print(f'{h}² = {c}² + c²')
            print(f'{h1} = {c1} + c²')
            print(f'c² = {s}')
            print(f'c = √{s}')
            print(f'Assim, chegando ao resultado de {raiz}.')
            print(f'hipotenusa = {h}, cateto oposto = {c} e', end=' ')
            print(f'cateto adjacente = {raiz} !')
        elif opção == 'H':
            limpar()
            print(txtc)
            print('Descobrindo a Hipotenusa.')
            co = int(input('Digite o primeiro cateto: '))
            ca = int(input('Digite o segundo cateto: '))
            co1 = math.pow(co, 2)
            ca1 = math.pow(ca, 2)
            s = co1 + ca1
            raiz = math.sqrt(s)
            print(f'A hipotenusa desse triângulo retângulo é {raiz}!')
            print(f'h² = {co}² + {ca}²')
            print(f'h² = {co1} + {ca1}')
            print(f'h² = {s}')
            print(f'h = √{s}')
            print(f'h = {raiz}')
            print(f'Assim, chegando ao resultado de {raiz}.')
            print(f'hipotenusa = {raiz}, cateto oposto = {co} e', end=' ')
            print(f'cateto adjacente = {ca} !')


    def Produtos():
        limpar()
        print(txtnot)
        print('Produtos Notáveis')
        opção = str(input(': '))
        while opção not in '123':
            opção = str(input(': '))
        if opção == '1':
            limpar()
            print(txtc)
            print('Quadrado da Soma')
            a = int(input('Digite o valor de a: '))
            b = int(input('Digite o valor de b: '))
            x = math.pow(a, 2)
            y = math.pow(b, 2)
            ab = 2 * a * b
            print('#' * 20)
            print(f'A operação digitada foi ({a} + {b})²')
            print('isso é igual a:')
            print(f'{x}x² + {ab}x + {y}')
        elif opção == '2':
            limpar()
            print(txtc)
            print('Quadrado da diferença')
            a = int(input('Digite o valor de a: '))
            b = int(input('Digite o valor de b: '))
            x = math.pow(a, 2)
            y = math.pow(b, 2)
            ab = 2 * a * b
            print('#' * 20)
            print(f'A operação digitada foi ({a} - {b})²')
            print('isso é igual a:')
            print(f'{x}x² - {ab}x + {y}')
        elif opção == '3':
            limpar()
            print(txtc)
            print('Produto da soma pela diferença')
            a = int(input('Digite o valor de a: '))
            b = int(input('Digite o valor de b: '))
            x = math.pow(a, 2)
            y = math.pow(b, 2)
            print('#' * 20)
            print(f'A operação foi = (a + b) . (a - b) = a² = b²')
            print('Por isso é igual a:')
            print(f'({a} + {b}) . ({a} - {b}) = {a}² - {b}² =', end='')
            print(f' {x} - {y}.')
    
    
    limpar()
    print(txt)
    opção = input(': ')
    while opção not in '12':
        opção = input(': ')
    if opção == '1':
        Pitagoras()
    elif opção == '2':
        Produtos()
