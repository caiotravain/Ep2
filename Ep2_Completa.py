import math
import random
def cria_baralho(): #Função cria o baralho
    baralho = []
    naipe = '\033[1;30m' +'♠' +'\033[1;97m' #Adiciona cor ao naipe
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
def empilha(lista,origem,destino): #Empilha a carta no baralho
    lista2 = []
    for count in range(len(lista)):
        if count == destino:
            lista2.append(lista[origem])
        elif count == origem:
            ''
        else:
            lista2.append(lista[count])
    return lista2
def extrai_naipe(x): #pega o naipe da carta
    if '♥' in x:
        return '♥'
    if '♦' in x:
        return '♦'
    if '♣' in x:
        return '♣'
    if '♠' in x:
        return '♠'
def extrai_valor(x):#pega o valor da carta
    if '10' in x:
        valor = x[:2]
    else:
        valor = x[:1]
    return valor
    return valor
def lista_movimentos_possiveis (baralho, indice): #mostra os movimentos possiveis
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
def possui_movimentos_possiveis (baralho): #mostra se tem algum movimento possivel
    for count in range(len(baralho)):
        tem =lista_movimentos_possiveis(baralho,count)
        if tem != []:
            return True
    return False
baralho = cria_baralho()
random.shuffle(baralho) #embaralha o baralho
t=1
jogar = input("Aperte enter para iniciar o jogo")
if jogar != '': #sai do jogo se não for apertado o enter
    quer = False
    print('Adeus')
else: 
    quer = True
if quer: #cria a condição para fazer o primeiro baralho
    for e in baralho: #escreve o baralho interio
        parte1 = '\033[1;97m' + str(t)
        print('{0}. {1}'.format(parte1, e))
        t+=1
while quer : #cria o loop do jogo
    qual_carta = (input('Digite a posição da carta na qual deseja mover ')) #carta na qual quer mover
    while qual_carta == '': #evita enter acidental
        print('Carta não encontrada')
        qual_carta = (input('Digite a posição da carta na qual deseja mover '))
    qual_carta = int(qual_carta)
    while qual_carta > len(baralho) or qual_carta< 1: #ve se existe a carta
        print('Carta não encontrada')
        qual_carta = (input('Escolha a carta na qual você quer empilhar:'))
    indice = qual_carta-1 #indice da carta
    tem_movimentos = lista_movimentos_possiveis (baralho, (indice)) #lista de movimentos
    if tem_movimentos != []:
        if len(tem_movimentos) == 1: #quando há só um movimento
            if tem_movimentos[0] == 1: #Quando o movimento é do lado da carta
                print('1. ' + baralho[indice-1])
                carta = int(input('Escolha a carta na qual você quer empilhar:'))
                while carta != 1: #Não deixa escolher carta não presente
                    print('Carta não encontrada')
                    carta = int(input('Escolha a carta na qual você quer empilhar:'))
                baralho = empilha(baralho,indice,indice-1)#empilha a carta
            else: #Quando o movimento é de tres espaços para tras
                print('1. ' + baralho[indice-3])
                carta = int(input('Escolha a carta na qual você quer empilhar:'))
                while carta != 1:#Não deixa escolher carta não presente
                    print('Carta não encontrada')
                    carta = int(input('Escolha a carta na qual você quer empilhar:'))
                baralho = empilha(baralho,indice,indice-3) #empilha a carta
        elif len(tem_movimentos) == 2: #Quando há dois movimentos
            print('1. ' + baralho[indice -1])
            print('2. ' + baralho[indice -3])
            carta = int(input('Escolha a carta na qual você quer empilhar:'))  
            while carta != 1 and carta!=2:#Não deixa escolher carta não presente
                print('Carta não encontrada')
                carta = int(input('Escolha a carta na qual você quer empilhar:'))
            if carta == 1:  #Quando o movimento é do lado da carta  
                baralho = empilha(baralho,indice,indice-1)#empilha a carta
            elif carta ==2:#Quando o movimento é de tres espaços para tras
                baralho = empilha(baralho,indice,indice-3)#empilha a carta
            else:
                print('Carta não encontrada')
        t=1
        for e in baralho: #escreve o baralho já empilhado
            print(str(t) + '. ' + e)
            t+=1
    else: # se não há movimentos para a carta escolhida
        print('Você não tem movimentos para essa carta')
    if len(baralho) == 1: #se há somente uma carta define o ganhador
        print('Parabens você Ganhou!')
        continua = input('Digite 1 para sair e 2 para jogar novamente')#se quiser jogar novamente ou sair
        if continua == '2':
            quer= True
        else:
            quer =False
    elif possui_movimentos_possiveis (baralho) == False:#não há mais movimentos declara-se perdedor
        print('Você perdeu...')
        continua = input('Digite 1 para sair e 2 para jogar novamente')#se quiser jogar novamente ou sair
        if continua == '2':
            quer= True
        else:
            quer =False
    if quer == False: #se não irá mais jogar Adeus!
        print('Adeus')
        
