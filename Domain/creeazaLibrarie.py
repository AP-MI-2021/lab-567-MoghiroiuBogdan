def creeaza_librarie(id, titlu, gen, pret, tipReducere):
    '''

    :param id:strig
    :param titlu:string
    :param gen:string
    :param pret:float
    :param tipReducere:string
    :return:
    '''

    return {
        "id": id,
        "titlu": titlu,
        "gen": gen,
        "pret": pret,
        "tipReducere": tipReducere

    }


def getId(librarie):
    return librarie["id"]


def getTitlu(librarire):
    return librarire["titlu"]


def getGen(librarie):
    return librarie["gen"]


def getPret(librarie):
    return librarie["pret"]


def getTipReducere(librarie):
    return librarie["tipReducere"]


def toString(librarie):
    return "id: {}, titlu:{}, gen:{}, pret:{}, tipReducere:{}".format(
        getId(librarie),
        getTitlu(librarie),
        getGen(librarie),
        getPret(librarie),
        getTipReducere(librarie),
    )
