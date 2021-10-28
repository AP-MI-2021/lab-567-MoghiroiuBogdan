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
    carte = creeaza_librarie(id, titlu, gen, pret, tipReducere)
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

    l=[]

    for x in lista:
        if getId(x) == id:
            cartenoua = creeaza_librarie(id, titlu, gen, pret, tipReducere)
            l.append(cartenoua)
        else:
            l.append(x)
    return l


