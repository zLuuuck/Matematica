import os
import platform


### Limpa o terminal
def limpar():
    sistema = platform.system()
    if sistema == 'Windows':
        os.system('cls')
    elif sistema == 'Linux':
        os.system('clear')

### texto de incio  ( texto principal )
txt = '''
|￣￣￣￣￣￣ |   O que deseja?
| Programa de|   [1] Matemática Básica
| Matemática |   [2] Matemática Diferenciada
|   do Z     |   [3] Conversores
| ___________|   [4] Física ( Em Breve )
(\__/)||
(•ㅅ•)||
/    づ

########### CRIADO POR zLuuuck#0996 ############

########### OBRIGADO  POR UTILIZAR ! ###########

'''
limpar()
print(txt)

opção = input(': ').strip()

while opção not in '1234':
    opção = input(': ').strip()

if opção == '1':
    from Scripts import MatematicaBásica
    MatematicaBásica.MatemáticaBásica
elif opção == '2':
    from Scripts import MatematicaDiferente
    MatematicaDiferente.MatematicaDiferenciada
elif opção == '3':
    from Scripts import Conversores
    Conversores.Conversores
elif opção == '4':
    print('Em desenvolvimento . . ')

rodar = input('\nDeseja rodar o programa novamente? [S/N] ').upper()
while rodar not in 'SN':
    rodar = input('\nDeseja rodar o programa novamente? [S/N] ').upper()
if rodar in 'S':
    limpar()
    os.system('python3 main.py')
elif rodar in 'N':
    print('finalizando . . ')
    limpar()
