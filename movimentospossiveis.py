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
    valor = x[:-1]
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
