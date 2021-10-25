from Domain.creeazaLibrarie import creeaza_librarie, getId


def adauga_carte(id, titlu, gen, pret, tipReducere,lista):
    carte = creeaza_librarie(id, titlu, gen, pret, tipReducere)
    return lista + [carte]


def get_by_id(id,lista):
    for carte in lista:
        if getId(carte) == id:
            return carte
    return None


def stergere_carte(id, lista):

    return [carte for carte in lista if getId(carte) != id]


def modifica_carte(id, titlu, gen, pret, tipReducere,lista):

    l=[]

    for x in lista:
        if getId(x) == id:
            cartenoua = creeaza_librarie(id, titlu, gen, pret, tipReducere)
            l.append(cartenoua)
        else:
            l.append(x)
    return l






