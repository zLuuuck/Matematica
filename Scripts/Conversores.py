import os
import platform

def limpar():
    sistema = platform.system()
    if sistema == 'Windows':
        os.system('cls')
    elif sistema == 'Linux':
        os.system('clear')

txt = '''
|￣￣￣￣￣￣ |   O que deseja?
| Programa de|   [1] Medidas
| Matemática |   [2] Massas
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
class Conversores:
    def medidas():
        limpar()
        print(txt)
        print('Conversor de medidas')
        metro = float(input('Digite um medida: '))
        tipo = str(input('Digite o tipo da medida: ')).lower()
        if tipo ==  'mm':
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

        elif tipo == 'cm':
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

        elif tipo == 'dm':
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

        elif tipo == 'm':
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

        elif tipo == 'dam':
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

        elif tipo == 'hm':
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

        elif tipo == 'km':
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
            
    
    def peso():
        limpar()
        print(txtc)
        print('Conversor de Massas')
        peso = float(input('Digite um peso: '))
        tipo = str(input('Digite o tipo da medida: ')).lower()

        if tipo ==  'mg':
            mg   = peso
            cg = peso / 10
            dg = peso / 100
            g = peso / 1000
            dag = peso / 100000
            hg = peso / 1000000
            kg = peso / 10000000
            print(f'A medida de {peso} {tipo} corresponde a:')
            print(f'{kg}kg, Kilogramas')
            print(f'{hg}hg, Hectograma')
            print(f'{dag}dag, Decagrama')
            print(f'{g},g Grama')
            print(f'{dg}dg, Decigrama')
            print(f'{cg}cg, Centigrama')
            print(f'{mg}mg, Miligrama')

        elif tipo == 'cg':
            mg = peso * 10
            cg = peso
            dg = peso / 10
            g = peso / 100
            dag = peso / 1000
            hg = peso / 10000
            kg = peso / 1000000
            print(f'A medida de {peso} {tipo} corresponde a:')
            print(f'{kg}kg, Kilogramas')
            print(f'{hg}hg, Hectograma')
            print(f'{dag}dag, Decagrama')
            print(f'{g},g Grama')
            print(f'{dg}dg, Decigrama')
            print(f'{cg}cg, Centigrama')
            print(f'{mg}mg, Miligrama')

        elif tipo == 'dg':
            mg = peso * 100
            cg = peso * 10
            dg = peso
            g = peso / 10
            dag = peso / 100
            hg = peso / 1000
            kg = peso / 10000
            print(f'A medida de {peso} {tipo} corresponde a:')
            print(f'{kg}kg, Kilogramas')
            print(f'{hg}hg, Hectograma')
            print(f'{dag}dag, Decagrama')
            print(f'{g},g Grama')
            print(f'{dg}dg, Decigrama')
            print(f'{cg}cg, Centigrama')
            print(f'{mg}mg, Miligrama')

        elif tipo == 'g':
            mg = peso * 1000
            cg = peso * 100
            dg = peso * 10
            g = peso 
            dag = peso / 10
            hg = peso / 100
            kg = peso / 1000
            print(f'A medida de {peso} {tipo} corresponde a:')
            print(f'{kg}kg, Kilogramas')
            print(f'{hg}hg, Hectograma')
            print(f'{dag}dag, Decagrama')
            print(f'{g},g Grama')
            print(f'{dg}dg, Decigrama')
            print(f'{cg}cg, Centigrama')
            print(f'{mg}mg, Miligrama')

        elif tipo == 'dag':
            mg = peso * 10000
            cg = peso * 1000
            dg = peso * 100
            g = peso * 10
            dag = peso 
            hg = peso / 10
            kg = peso / 100
            print(f'A medida de {peso} {tipo} corresponde a:')
            print(f'{kg}kg, Kilogramas')
            print(f'{hg}hg, Hectograma')
            print(f'{dag}dag, Decagrama')
            print(f'{g},g Grama')
            print(f'{dg}dg, Decigrama')
            print(f'{cg}cg, Centigrama')
            print(f'{mg}mg, Miligrama')

        elif tipo == 'hg':
            mg = peso * 100000
            cg = peso * 10000
            dg = peso * 1000
            g = peso * 100
            dag = peso * 10
            hg = peso 
            kg = peso / 10
            print(f'A medida de {peso} {tipo} corresponde a:')
            print(f'{kg}kg, Kilogramas')
            print(f'{hg}hg, Hectograma')
            print(f'{dag}dag, Decagrama')
            print(f'{g},g Grama')
            print(f'{dg}dg, Decigrama')
            print(f'{cg}cg, Centigrama')
            print(f'{mg}mg, Miligrama')

        elif tipo == 'kg':
            mg = peso * 1000000
            cg = peso * 100000
            dg = peso * 10000
            g = peso * 1000
            dag = peso * 100
            hg = peso * 10
            kg = peso 
            print(f'A medida de {peso} {tipo} corresponde a:')
            print(f'{kg}kg, Kilogramas')
            print(f'{hg}hg, Hectograma')
            print(f'{dag}dag, Decagrama')
            print(f'{g},g Grama')
            print(f'{dg}dg, Decigrama')
            print(f'{cg}cg, Centigrama')
            print(f'{mg}mg, Miligrama')
    

    limpar()
    print(txt)
    opção = input(': ')
    while opção not in '12':
        opção = input(': ')
    if opção == '1':
        medidas()
    elif opção == '2':
        peso()
