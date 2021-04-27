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