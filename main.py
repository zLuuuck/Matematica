import os
import time

print('Loading…')
time.sleep(0.5)
print('30%')
print('███▒▒▒▒▒▒▒')
time.sleep(0.5)
print('50%')
print('█████▒▒▒▒▒')
time.sleep(0.5)
print('80%')
print('████████▒▒')
time.sleep(0.5)
print('100%')
print('██████████')
time.sleep(1.5)
os.system('clear')

############################################################
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

############################################################

def desconto():
    os.system('clear')
    print(txt2)
    preço = float(input('Digite o preço do produto: R$'))
    des = float(input('Digite o a % do desconto: '))
    novo = preço - (preço * des / 100)
    totaldes = novo - preço

    print(f'O preço é R${preço}, com um desconto de {des}%, fica R${novo}.')
    print(f'O desconto é de {totaldes}')

    print('')

############################################################

def aumento():
    os.system('clear')
    print(txt2)
    sal = float(input('Digite o seu salário, ou um valor qualquer(use com "." invés de ","): R$'))
    aumento = float(input('Digite a % do aumento: '))
    novo = sal + (sal * aumento / 100)
    totalau = sal - novo

    print(f'Seu salário/valor é de R${sal}. Você ganhou {aumento}% de aumento,', end=' ')
    print(f'agora ele é de R${novo:.2f}')
    print(f'Ganhou-se {totalau}')
    
############################################################

def medidas():
    os.system('clear')
    print(txt2)
    metro = float(input('Digite uma distância em metros: '))
    dm = metro * 10
    cm = metro * 100
    mm = metro * 1000
    dam = metro / 10
    hm = metro / 100
    km = metro / 1000
    print(f'A medida de {metro}m corresponde a \n{km}km \n{hm}hm \n', end='')
    print(f'{dam}dam \n{dm}dm \n{cm}cm \n{mm}mm')
    
############################################################

def pitagoras():
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

############################################################

def pitagorasIn():
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
    
############################################################
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
    [1] tabuada
    [2] desconto em porcentagem
    [3] aumento em porcentagem
    [4] pitagoras
    [5] pitagoras com hipotenusa
    [6] medidas
    [7] física (Não desenvolvido)
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
print(txt)
od = input(': ')
if od == '1':
    tabuada()
elif od == '2':
    desconto()
elif od == '3':
    aumento()
elif od == '4':
    pitagoras()
elif od == '5':
    pitagorasIn()
elif od == '6':
    medidas()
elif od == '7':
    print('não ta desenvolvido')
    varad = "Saindo em 3.."
    print(varad)
    time.sleep(1)
    varad = "Saindo em 32."
    print(varad)
    time.sleep(1)
    varad = "Saindo em 321"
    print(varad, 'fechando..')
    time.sleep(1)
    os.system('clear')
else:

  print("a ok")
  
pg = input('\nDeseja fazer uma nova consulta? [sim][nao]')
if pg == 'sim' or pg == 'SIM' or pg == 's' or pg == 'S':
    os.system('clear')
    os.system('python3 main.py')
elif pg == 'nao' or pg== 'NAO' or pg== 'n' or pg== 'N':
    varad = "Adeus em 3.."
    print(varad)
    time.sleep(1)
    varad = "Adeus em 32."
    print(varad)
    time.sleep(1)
    varad = "Adeus em 321"
    print(varad, 'fechando..')
    time.sleep(1)
    os.system('clear')
