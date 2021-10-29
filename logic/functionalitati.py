from Domain.creeazaLibrarie import getTipReducere, creeaza_librarie, getId, getTitlu, getGen, getPret


def discount(lista):
    '''
    creeaza discount de 5% pt reducere de tip silver si de 10 % pe cea de tip gold
    :param lista:
    :return: lista dupa reducere
    '''

    l = []
    for carte in lista:
        if getTipReducere(carte) == "silver":
            cartenoua = creeaza_librarie(getId(carte),
                                         getTitlu(carte),
                                         getGen(carte),
                                         getPret(carte) - getPret(carte) * 0.05,
                                         getTipReducere(carte),
                                         )
            l.append(cartenoua)
        elif getTipReducere(carte) == "gold":
            cartenoua = creeaza_librarie(getId(carte),
                                         getTitlu(carte),
                                         getGen(carte),
                                         getPret(carte) - getPret(carte) * 0.1,
                                         getTipReducere(carte),
                                         )
            l.append(cartenoua)
        else:
            l.append(carte)
    return l


def modifica_genul(title, lista, noulgen):
    l = []
    for carte in lista:
        if getTitlu(carte) == title:
            listanoua = creeaza_librarie(getId(carte),
                                         getTitlu(carte),
                                         noulgen,
                                         getPret(carte),
                                         getTipReducere(carte),
                                         )
            l.append(listanoua)
        else:
            l.append(carte)
    return l


def pret_minim(lista):
    rez={}

    for carte in lista:
        gen = getGen(carte)
        pret = getPret(carte)
        if gen in rez:
            if pret < rez[gen]:
                rez[gen] = pret
        else:
            rez[gen] = pret

    return rez


def ordoneaza_crescator(lista):
    pass
