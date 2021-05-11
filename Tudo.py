import math
import random
def cria_baralho():
    baralho = []
    naipe = '\033[1;30m' +'♠' +'\033[1;97m'
    count = 0
    t=1
    while count < 4:    
        if count == 1:
            naipe = '\033[1;31m'+'♥'+'\033[1;97m'
        if count == 2:
            naipe = '\033[1;31m' + '♦'+'\033[1;97m'
        if count == 3:
            naipe = '\033[1;30m' + '♣'+'\033[1;97m'
        if t > 13:
            t = 1
        while t <= 13:
            A = t
            if t ==11:
                A = 'J'
            elif t ==12:
                A = 'Q'
            elif t == 13:
                A = 'K'
            elif t ==1:
                A = 'A'
            baralho.append(str(A) + naipe)
            t +=1
        count +=1        
    return (baralho)
def empilha(lista,origem,destino):
    lista2 = []
    for count in range(len(lista)):
        if count == destino:
            lista2.append(lista[origem])
        elif count == origem:
            ''
        else:
            lista2.append(lista[count])
    return lista2
def extrai_naipe(x):
    if '♥' in x:
        return '♥'
    if '♦' in x:
        return '♦'
    if '♣' in x:
        return '♣'
    if '♠' in x:
        return '♠'
def extrai_valor(x):
    if '10' in x:
        valor = x[:2]
    else:
        valor = x[:1]
    return valor
    return valor
def lista_movimentos_possiveis (baralho, indice):
    movimentos = []
    if indice == 0:
        return movimentos
    if extrai_valor(baralho[indice]) == extrai_valor(baralho[indice-1]):
        movimentos.append(1)
    elif extrai_naipe(baralho[indice]) == extrai_naipe(baralho[indice-1]):
        movimentos.append(1)
    if extrai_naipe(baralho[indice]) == extrai_naipe(baralho[indice-3]) and ((indice-3) >= 0) :
        movimentos.append(3)
    elif extrai_valor(baralho[indice]) == extrai_valor(baralho[indice-3]) and ((indice-3) >= 0) :
        movimentos.append(3)
    return movimentos
def possui_movimentos_possiveis (baralho):
    for count in range(len(baralho)):
        tem =lista_movimentos_possiveis(baralho,count)
        if tem != []:
            return True
    return False
baralho = cria_baralho()
random.shuffle(baralho)
t=1
jogar = input("Aperte enter para iniciar o jogo")
if jogar != '':
    quer = False
    print('Adeus')
else: 
    quer = True
if quer:
    for e in baralho:
        parte1 = '\033[1;97m' + str(t)
        print('{0}. {1}'.format(parte1, e))
        t+=1
while quer :
    qual_carta = int(input('Digite a posição da carta na qual deseja mover '))
    while qual_carta > len(baralho) or qual_carta< 1:
        print('Carta não encontrada')
        qual_carta = int(input('Escolha a carta na qual você quer empilhar:'))
    indice = qual_carta-1 
    tem_movimentos = lista_movimentos_possiveis (baralho, (indice))
    if tem_movimentos != []:
        if len(tem_movimentos) == 1:
            if tem_movimentos[0] == 1:    
                print('1. ' + baralho[indice-1])
                carta = int(input('Escolha a carta na qual você quer empilhar:'))
                while carta != 1:
                    print('Carta não encontrada')
                    carta = int(input('Escolha a carta na qual você quer empilhar:'))
                baralho = empilha(baralho,indice,indice-1)
            else:
                print('1. ' + baralho[indice-3])
                carta = int(input('Escolha a carta na qual você quer empilhar:'))
                while carta != 1:
                    print('Carta não encontrada')
                    carta = int(input('Escolha a carta na qual você quer empilhar:'))
                baralho = empilha(baralho,indice,indice-3)
        elif len(tem_movimentos) == 2:
            print('1. ' + baralho[indice -1])
            print('2. ' + baralho[indice -3])
            carta = int(input('Escolha a carta na qual você quer empilhar:'))  
            while carta != 1 and carta!=2:
                print('Carta não encontrada')
                carta = int(input('Escolha a carta na qual você quer empilhar:'))
            if carta == 1:    
                baralho = empilha(baralho,indice,indice-1)
            elif carta ==2:
                baralho = empilha(baralho,indice,indice-3)
            else:
                print('Carta não encontrada')
        t=1
        for e in baralho:
            print(str(t) + '. ' + e)
            t+=1
    else: 
        print('Você não tem movimentos para essa carta')
    if len(baralho) == 1:
        print('Parabens você Ganhou!')
    if possui_movimentos_possiveis (baralho) == False:
        print('Você perdeu...')
        continua = input('Digite 1 para sair e 2 para jogar novamente')
        if continua == '1':
            quer= True
        else:
            quer =False
        
