def cria_baralho():
    baralho = []
    naipe = '♠'
    count = 0
    t=1
    while count < 4:    
        if count == 1:
            naipe ='♥'
        if count == 2:
            naipe = '♦'
        if count == 3:
            naipe = '♣'
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
print(cria_baralho())
