import os
import time


def tabuada():
    os.system('clear')
    print(txt2)
    nu = int(input('Digite um número:'))

    x1 = nu * 1
    x2 = nu * 2
    x3 = nu * 3
    x4 = nu * 4
    x5 = nu * 5
    x6 = nu * 6
    x7 = nu * 7
    x8 = nu * 8
    x9 = nu * 9
    x10 = nu * 10
    x11 = nu * 11
    x12 = nu * 12
    x13 = nu * 13
    x14 = nu * 14
    x15 = nu * 15
    x16 = nu * 16
    x17 = nu * 17
    x18 = nu * 18
    x19 = nu * 19
    x20 = nu * 20
    x21 = nu * 21
    x22 = nu * 22
    x23 = nu * 23
    x24 = nu * 24
    x25 = nu * 25
    x26 = nu * 26
    x27 = nu * 27
    x28 = nu * 28
    x29 = nu * 29
    x30 = nu * 30
    x31 = nu * 31
    x32 = nu * 32
    x33 = nu * 33
    x34 = nu * 34
    x35 = nu * 35
    x36 = nu * 36
    x37 = nu * 37
    x38 = nu * 38
    x39 = nu * 39
    x40 = nu * 40
    x41 = nu * 41
    x42 = nu * 42
    x43 = nu * 43
    x44 = nu * 44
    x45 = nu * 45
    x46 = nu * 46
    x47 = nu * 47
    x48 = nu * 48
    x49 = nu * 49
    x50 = nu * 50
    print(f'A tabuada de {nu} é: ')
    print(f'{nu}x 1 = {x1}')
    print(f'{nu}x 2 = {x2}')
    print(f'{nu}x 3 = {x3}')
    print(f'{nu}x 4 = {x4}')
    print(f'{nu}x 5 = {x5}')
    print(f'{nu}x 6 = {x6}')
    print(f'{nu}x 7 = {x7}')
    print(f'{nu}x 8 = {x8}')
    print(f'{nu}x 9 = {x9}')
    print(f'{nu}x10 = {x10}')
    print(f'{nu}x11 = {x11}')
    print(f'{nu}x12 = {x12}')
    print(f'{nu}x13 = {x13}')
    print(f'{nu}x14 = {x14}')
    print(f'{nu}x15 = {x15}')
    print(f'{nu}x16 = {x16}')
    print(f'{nu}x17 = {x17}')
    print(f'{nu}x18 = {x18}')
    print(f'{nu}x19 = {x19}')
    print(f'{nu}x20 = {x20}')
    print(f'{nu}x21 = {x21}')
    print(f'{nu}x22 = {x22}')
    print(f'{nu}x23 = {x23}')
    print(f'{nu}x24 = {x24}')
    print(f'{nu}x25 = {x25}')
    print(f'{nu}x26 = {x26}')
    print(f'{nu}x27 = {x27}')
    print(f'{nu}x28 = {x28}')
    print(f'{nu}x29 = {x29}')
    print(f'{nu}x30 = {x30}')
    print(f'{nu}x31 = {x31}')
    print(f'{nu}x32 = {x32}')
    print(f'{nu}x33 = {x33}')
    print(f'{nu}x34 = {x34}')
    print(f'{nu}x35 = {x35}')
    print(f'{nu}x36 = {x36}')
    print(f'{nu}x37 = {x37}')
    print(f'{nu}x38 = {x38}')
    print(f'{nu}x39 = {x39}')
    print(f'{nu}x40 = {x40}')
    print(f'{nu}x41 = {x41}')
    print(f'{nu}x42 = {x42}')
    print(f'{nu}x43 = {x43}')
    print(f'{nu}x44 = {x44}')
    print(f'{nu}x45 = {x45}')
    print(f'{nu}x46 = {x46}')
    print(f'{nu}x47 = {x47}')
    print(f'{nu}x48 = {x48}')
    print(f'{nu}x49 = {x49}')
    print(f'{nu}x50 = {x50}')


def porcentagens():
    os.system('clear')
    print(txtPORCENT)
    opçãoPORCENT = int(input(': '))
    if opçãoPORCENT == 1:
        os.system('clear')
        print(txt2)
        preço = float(input('Digite o preço do produto: R$'))
        des = float(input('Digite o a % do desconto: '))
        novo = preço - (preço * des / 100)
        totaldes = preço - novo

        print(f'O preço é R${preço}, com um desconto de {des}%, fica R${novo}.')
        print(f'O desconto é de {totaldes}')

    elif opçãoPORCENT == 2:
        os.system('clear')
        print(txt2)
        sal = float(input(
            'Digite o seu salário, ou um valor qualquer(use com "." invés de ","): R$'))
        aumento = float(input('Digite a % do aumento: '))
        novo = sal + (sal * aumento / 100)
        totalau = novo - sal

        print(
            f'Seu salário/valor é de R${sal}. Você ganhou {aumento}% de aumento,', end=' ')
        print(f'agora ele é de R${novo:.2f}')
        print(f'Ganhou-se {totalau}')
    else:
        print("a ok")

    rodar_dnv = input('\nDeseja rodar o programa novamente? s/n: ')
    if rodar_dnv == 'sim' or rodar_dnv == 'SIM' or rodar_dnv == 's' or rodar_dnv == 'S':
        os.system('clear')
        os.system('python3 main.py')
    elif rodar_dnv == 'nao' or rodar_dnv == 'NAO' or rodar_dnv == 'n' or rodar_dnv == 'N':
        time.sleep(1)
        print('fechando..')
        time.sleep(1)
        os.system('clear')


def potencia():
    import math
    os.system('clear')
    print(txt2)
    num = int(input('Digite o número: '))
    ex = int(input('Digite o expoente: '))
    pot = math.pow(num, ex)
    print(f'O resultado de sua conta é {pot}')


def medidas():
    os.system('clear')
    print(txt2)
    metro = float(input('Digite um medida: '))
    tipo = str(input('Digite o tipo da medida: '))

    if tipo == 'mm' or tipo == 'milímetros' or tipo == 'MM':
        mm = metro
        cm = metro / 10
        dm = metro / 100
        m = metro / 1000
        dam = metro / 10000
        hm = metro / 100000
        km = metro / 1000000
        print(f'A medida de {metro} {tipo} corresponde a:')
        print(f'{km}km, Quilômetros')
        print(f'{hm}hm, Hectomêtro')
        print(f'{dam}dam, Decametro')
        print(f'{m}m, Metros')
        print(f'{dm}dm, Decimetro')
        print(f'{cm}cm, Centimetros')
        print(f'{mm}mm, Milímetros')

    elif tipo == 'cm' or tipo == 'centimetros' or tipo == 'CM':
        mm = metro * 10
        cm = metro
        dm = metro / 10
        m = metro / 100
        dam = metro / 1000
        hm = metro / 10000
        km = metro / 100000
        print(f'A medida de {metro} {tipo} corresponde a:')
        print(f'{km}km, Quilômetros')
        print(f'{hm}hm, Hectomêtro')
        print(f'{dam}dam, Decametro')
        print(f'{m}m, Metros')
        print(f'{dm}dm, Decimetro')
        print(f'{cm}cm, Centimetros')
        print(f'{mm}mm, Milímetros')

    elif tipo == 'dm' or tipo == 'decimetro' or tipo == 'DM':
        mm = metro * 100
        cm = metro * 10
        dm = metro
        m = metro / 10
        dam = metro / 100
        hm = metro / 1000
        km = metro / 10000
        print(f'A medida de {metro} {tipo} corresponde a:')
        print(f'{km}km, Quilômetros')
        print(f'{hm}hm, Hectomêtro')
        print(f'{dam}dam, Decametro')
        print(f'{m}m, Metros')
        print(f'{dm}dm, Decimetro')
        print(f'{cm}cm, Centimetros')
        print(f'{mm}mm, Milímetros')

    elif tipo == 'm' or tipo == 'metro' or tipo == 'M':
        dm = metro * 10
        cm = metro * 100
        mm = metro * 1000
        m = metro
        dam = metro / 10
        hm = metro / 100
        km = metro / 1000
        print(f'A medida de {metro} {tipo} corresponde a:')
        print(f'{km}km')
        print(f'{hm}hm')
        print(f'{dam}dam')
        print(f'{m}m ')
        print(f'{dm}dm')
        print(f'{cm}cm')
        print(f'{mm}mm')

    elif tipo == 'dam' or tipo == 'decametro' or tipo == 'DAM':
        mm = metro * 10000
        cm = metro * 1000
        dm = metro * 100
        m = metro * 10
        dam = metro
        hm = metro / 10
        km = metro / 100
        print(f'A medida de {metro} {tipo} corresponde a:')
        print(f'{km}km, Quilômetros')
        print(f'{hm}hm, Hectomêtro')
        print(f'{dam}dam, Decametro')
        print(f'{m}m, Metros')
        print(f'{dm}dm, Decimetro')
        print(f'{cm}cm, Centimetros')
        print(f'{mm}mm, Milímetros')

    elif tipo == 'hm' or tipo == 'hectometro' or tipo == 'HM':
        mm = metro * 100000
        cm = metro * 10000
        dm = metro * 1000
        m = metro * 100
        dam = metro * 10
        hm = metro
        km = metro / 10
        print(f'A medida de {metro} {tipo} corresponde a:')
        print(f'{km}km, Quilômetros')
        print(f'{hm}hm, Hectomêtro')
        print(f'{dam}dam, Decametro')
        print(f'{m}m, Metros')
        print(f'{dm}dm, Decimetro')
        print(f'{cm}cm, Centimetros')
        print(f'{mm}mm, Milímetros')

    elif tipo == 'km' or tipo == 'kilometros' or tipo == 'KM':
        mm = metro * 1000000
        cm = metro * 100000
        dm = metro * 10000
        m = metro * 1000
        dam = metro * 100
        hm = metro * 10
        km = metro
        print(f'A medida de {metro} {tipo} corresponde a:')
        print(f'{km}km, Quilômetros')
        print(f'{hm}hm, Hectomêtro')
        print(f'{dam}dam, Decametro')
        print(f'{m}m, Metros')
        print(f'{dm}dm, Decimetro')
        print(f'{cm}cm, Centimetros')
        print(f'{mm}mm, Milímetros')


def pitagoras():
    os.system('clear')
    print(txtPIT)
    opçãoPIT = int(input(': '))

    if opçãoPIT == 1:
        os.system('clear')
        print(txt2)
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
    elif opçãoPIT == 2:
        os.system('clear')
        print(txt2)
        import math

        H = int(input('Digite a hipotenusa: '))
        C = int(input('Digite o cateto: '))

        H1 = math.pow(H, 2)
        C1 = math.pow(C, 2)
        scateto = H1 - C1
        raiz = math.sqrt(scateto)
        h = math.ceil(raiz)

        print(f'O Cateto desse triângulo retângulo é {h}.')
        print(f'{H}² = {C}² + C²')
        print(f'{H1} = {C1} + C²')
        time.sleep(1)
        print('Agora, nós invertemos a operação.')
        time.sleep(1)
        print(f'{H1} - {C1} = C²')
        print(f'{scateto} = C²')
        time.sleep(1)
        print('Agora, fazeremos a conta inversa, transformando a potencia (C²), em raiz quadrada (²√).')
        time.sleep(1)
        print(f'C = ²√{scateto}')
        print(f'Obtendo assim, o resultado de {h}.')
        print(f'Sendo assim, o Cateto desconhecido tem o valor de {h}')

    else:
        print("a ok")

    rodar_dnv = input('\nDeseja rodar o programa novamente? s/n: ')
    if rodar_dnv == 'sim' or rodar_dnv == 'SIM' or rodar_dnv == 's' or rodar_dnv == 'S':
        os.system('clear')
        os.system('python3 main.py')
    elif rodar_dnv == 'nao' or rodar_dnv == 'NAO' or rodar_dnv == 'n' or rodar_dnv == 'N':
        adeus = "Adeus em 3.."
        print(adeus)
        time.sleep(1)
        adeus = "Adeus em 32."
        print(adeus)
        time.sleep(1)
        adeus = "Adeus em 321"
        print(adeus, 'fechando..')
        time.sleep(1)
        os.system('clear')


def raiz4():
    os.system('clear')
    print(txt2)
    import math
    num = int(input('Digite o número: '))
    resultado = math.sqrt(num)
    print(f'O resultado da sua conta é {resultado}!')


def prodNot():
    os.system('clear')
    print(txt2)
    txtNOT = """
    █▄░▄█ ▄▀▄ ▀█▀ █▀▀ █▄░▄█ ▄▀▄ ▀█▀ ▀ ▄▀ ▄▀▄
    █░█░█ █▀█ ░█░ █▀▀ █░█░█ █▀█ ░█░ █ █░ █▀█
    ▀░░░▀ ▀░▀ ░▀░ ▀▀▀ ▀░░░▀ ▀░▀ ░▀░ ▀ ░▀ ▀░▀
                    █▀▄ ▄▀▄
                    █░█ █░█
                    ▀▀░ ░▀░
        ╔════╗     ╔╗───╔╗─╔╗╔╗─╔╗╔╗─╔╗╔═══╗╔╗╔═╗
        ╚══╗═║     ║║───║║─║║║║─║║║║─║║║╔═╗║║║║╔╝
        ──╔╝╔╝     ║║───║║─║║║║─║║║║─║║║║─╚╝║╚╝╝─
        ─╔╝╔╝─     ║║─╔╗║║─║║║║─║║║║─║║║║─╔╗║╔╗║─
        ╔╝═╚═╗     ║╚═╝║║╚═╝║║╚═╝║║╚═╝║║╚═╝║║║║╚╗
        ╚════╝     ╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝╚╝╚═╝
        Área de Produtos Notáveis.

        [ 1 ] Quadrado da soma
        [ 2 ] Quadrado da diferença

    """
    import math
    print(txtNOT)
    opNOT = input(': ')
    if opNOT == '1':
        os.system('clear')
        print(txt2)
        print('Se o X estiver sozinho, coleque 1, mas se tiver algum valor, coloque o valor de X.')
        print('O programa imprime todas as repostas com o valor de X')
        a = int(input('Digite o valor de X: '))
        b = int(input('Digite o valor do segundo número: '))
        # (a + b)² = a² + 2ab + b²
        x = math.pow(a, 2)
        y = math.pow(b, 2)
        ab = 2 * a * b
        print('#' * 20)
        print(f'A operação digitada foi ({a} + {b})²')
        print('isso é igual a:')
        print(f'{x}x² + {ab}x + {y}')
    elif opNOT == '2':
        os.system('clear')
        print(txt2)
        print('Se o X estiver sozinho, coleque 1, mas se tiver algum valor, coloque o valor de X.')
        print('O programa imprime todas as repostas com o valor de X')
        a = int(input('Digite o valor de X: '))
        b = int(input('Digite o valor do segundo número: '))
        # (a + b)² = a² - 2ab + b²
        x = math.pow(a, 2)
        y = math.pow(b, 2)
        ab = 2 * a * b
        print('#' * 20)
        print(f'A operação digitada foi ({a}x - {b})²')
        print('isso é igual a:')
        print(f'{x}x² - {ab}x + {y}')


txt = """

|￣￣￣￣￣￣ |
| Programa de|
| Matemática |
|   do Z     |
| ___________|
(\__/) ||
(•ㅅ•) ||
/    づ
█▄░▄█ ▄▀▄ ▀█▀ █▀▀ █▄░▄█ ▄▀▄ ▀█▀ ▀ ▄▀ ▄▀▄
█░█░█ █▀█ ░█░ █▀▀ █░█░█ █▀█ ░█░ █ █░ █▀█
▀░░░▀ ▀░▀ ░▀░ ▀▀▀ ▀░░░▀ ▀░▀ ░▀░ ▀ ░▀ ▀░▀
                █▀▄ ▄▀▄
                █░█ █░█
                ▀▀░ ░▀░
╔════╗     ╔╗─── ╔╗─╔╗ ╔╗─╔╗ ╔╗─╔╗ ╔═══╗ ╔╗╔═╗
╚══╗═║     ║║─── ║║─║║ ║║─║║ ║║─║║ ║╔═╗║ ║║║╔╝
──╔╝╔╝     ║║─── ║║─║║ ║║─║║ ║║─║║ ║║─╚╝ ║╚╝╝─
─╔╝╔╝─     ║║─╔╗ ║║─║║ ║║─║║ ║║─║║ ║║─╔╗ ║╔╗║─
╔╝═╚═╗     ║╚═╝║ ║╚═╝║ ║╚═╝║ ║╚═╝║ ║╚═╝║ ║║║╚╗
╚════╝     ╚═══╝ ╚═══╝ ╚═══╝ ╚═══╝ ╚═══╝ ╚╝╚═╝

######### CRIADO POR (! Z Luuuck#0996) #########

########### OBRIGADO  POR UTILIZAR ! ###########

    o que deseja?
    [ 1 ] Tabuada
    [ 2 ] Porcentagens
    [ 3 ] Potencia
    [ 4 ] Pitagoras
    [ 5 ] Raiz Quadrada
    [ 6 ] Medidas
    [ 7 ] Física (Não desenvolvido)
    [ 8 ] Produtos Notáveis

"""


txt2 = """
 █▄░▄█ ▄▀▄ ▀█▀ █▀▀ █▄░▄█ ▄▀▄ ▀█▀ ▀ ▄▀ ▄▀▄
 █░█░█ █▀█ ░█░ █▀▀ █░█░█ █▀█ ░█░ █ █░ █▀█
 ▀░░░▀ ▀░▀ ░▀░ ▀▀▀ ▀░░░▀ ▀░▀ ░▀░ ▀ ░▀ ▀░▀
                 █▀▄ ▄▀▄
                 █░█ █░█
                 ▀▀░ ░▀░
    ╔════╗     ╔╗───╔╗─╔╗╔╗─╔╗╔╗─╔╗╔═══╗╔╗╔═╗
    ╚══╗═║     ║║───║║─║║║║─║║║║─║║║╔═╗║║║║╔╝
    ──╔╝╔╝     ║║───║║─║║║║─║║║║─║║║║─╚╝║╚╝╝─
    ─╔╝╔╝─     ║║─╔╗║║─║║║║─║║║║─║║║║─╔╗║╔╗║─
    ╔╝═╚═╗     ║╚═╝║║╚═╝║║╚═╝║║╚═╝║║╚═╝║║║║╚╗
    ╚════╝     ╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝╚╝╚═╝
"""


txtPORCENT = """
 █▄░▄█ ▄▀▄ ▀█▀ █▀▀ █▄░▄█ ▄▀▄ ▀█▀ ▀ ▄▀ ▄▀▄
 █░█░█ █▀█ ░█░ █▀▀ █░█░█ █▀█ ░█░ █ █░ █▀█
 ▀░░░▀ ▀░▀ ░▀░ ▀▀▀ ▀░░░▀ ▀░▀ ░▀░ ▀ ░▀ ▀░▀
                 █▀▄ ▄▀▄
                 █░█ █░█
                 ▀▀░ ░▀░
    ╔════╗     ╔╗───╔╗─╔╗╔╗─╔╗╔╗─╔╗╔═══╗╔╗╔═╗
    ╚══╗═║     ║║───║║─║║║║─║║║║─║║║╔═╗║║║║╔╝
    ──╔╝╔╝     ║║───║║─║║║║─║║║║─║║║║─╚╝║╚╝╝─
    ─╔╝╔╝─     ║║─╔╗║║─║║║║─║║║║─║║║║─╔╗║╔╗║─
    ╔╝═╚═╗     ║╚═╝║║╚═╝║║╚═╝║║╚═╝║║╚═╝║║║║╚╗
    ╚════╝     ╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝╚╝╚═╝
    Área de Porcentagem.

    [ 1 ] Desconto
    [ 2 ] Aumento

"""

txtPIT = """
 █▄░▄█ ▄▀▄ ▀█▀ █▀▀ █▄░▄█ ▄▀▄ ▀█▀ ▀ ▄▀ ▄▀▄
 █░█░█ █▀█ ░█░ █▀▀ █░█░█ █▀█ ░█░ █ █░ █▀█
 ▀░░░▀ ▀░▀ ░▀░ ▀▀▀ ▀░░░▀ ▀░▀ ░▀░ ▀ ░▀ ▀░▀
                 █▀▄ ▄▀▄
                 █░█ █░█
                 ▀▀░ ░▀░
    ╔════╗     ╔╗───╔╗─╔╗╔╗─╔╗╔╗─╔╗╔═══╗╔╗╔═╗
    ╚══╗═║     ║║───║║─║║║║─║║║║─║║║╔═╗║║║║╔╝
    ──╔╝╔╝     ║║───║║─║║║║─║║║║─║║║║─╚╝║╚╝╝─
    ─╔╝╔╝─     ║║─╔╗║║─║║║║─║║║║─║║║║─╔╗║╔╗║─
    ╔╝═╚═╗     ║╚═╝║║╚═╝║║╚═╝║║╚═╝║║╚═╝║║║║╚╗
    ╚════╝     ╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝╚╝╚═╝
    Área de Pitagoras.

    [ 1 ] Pitagoras descobrindo hipotenusa
    [ 2 ] Pitagoras descobrindo cateto

"""
print(txt)
opção = input(': ')
if opção == '1':
    tabuada()
elif opção == '2':
    porcentagens()
elif opção == '3':
    potencia()
elif opção == '4':
    pitagoras()
elif opção == '5':
    raiz4()
elif opção == '6':
    medidas()
elif opção == '7':
    print('não ta desenvolvido')
    time.sleep(1)
    print('fechando..')
    time.sleep(1)
    os.system('clear')
elif opção == '8':
    prodNot()
else:
    print("a ok")

rodar_dnv = input('\nDeseja rodar o programa novamente? s/n: ')
if rodar_dnv == 'sim' or rodar_dnv == 'SIM' or rodar_dnv == 's' or rodar_dnv == 'S':
    os.system('clear')
    os.system('python3 main.py')
elif rodar_dnv == 'nao' or rodar_dnv == 'NAO' or rodar_dnv == 'n' or rodar_dnv == 'N':
    print('fechando..')
    time.sleep(1)
    os.system('clear')
