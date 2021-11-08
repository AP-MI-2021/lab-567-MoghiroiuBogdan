from Domain.creeazaLibrarie import creeaza_librarie, getId, getTipReducere, getPret


def adauga_carte(id, titlu, gen, pret, tipReducere,lista):
    '''
    adauga o carte noua
    :param id:
    :param titlu:
    :param gen:
    :param pret:
    :param tipReducere:
    :param lista:
    :return: lista
    '''
    if get_by_id(id,lista) is not None:
        raise ValueError(":id-ul este deja folosit")

    carte = creeaza_librarie(id, titlu, gen, pret, tipReducere)
    if getPret(carte) < 0:
        raise ValueError(":pretul este negativ! Incorect")
    if getTipReducere(carte) != "gold" and getTipReducere(carte) != "silver" and getTipReducere(carte) != "none":
        raise ValueError(":reducerea adaugata nu exista")
    return lista + [carte]


def get_by_id(id,lista):
    '''
    verifica daca o carte id ul dat este in lista
    :param id:
    :param lista:
    :return: none sau cartea cu id ul cautat
    '''
    for carte in lista:
        if getId(carte) == id:
            return carte
    return None


def stergere_carte(id, lista):
    '''
    sterge o carte din lista 
    :param id:
    :param lista:
    :return: lista noua
    '''
    if get_by_id(id,lista) is None:
        raise ValueError(":cartea pe care vrei sa o stergi nu exista!")
    return [carte for carte in lista if getId(carte) != id]


def modifica_carte(id, titlu, gen, pret, tipReducere,lista):
    '''
    modifica o carte din lista in functie de un id dat
    :param id:
    :param titlu:
    :param gen:
    :param pret:
    :param tipReducere:
    :param lista:
    :return: lista modificata
    '''
    if get_by_id(id,lista) is None:
        raise ValueError (":nu exista o carte cu id-ul dat")

    l=[]

    for x in lista:
        if getId(x) == id:
            cartenoua = creeaza_librarie(id, titlu, gen, pret, tipReducere)
            if getPret(cartenoua) < 0:
                raise ValueError (":pretul este negativ! Incorect")
            if getTipReducere(cartenoua) != "gold" and getTipReducere(cartenoua) != "silver" and getTipReducere(cartenoua) != "none" :
                raise ValueError (":reducerea adaugata nu exista")
            l.append(cartenoua)
        else:
            l.append(x)
    return l

