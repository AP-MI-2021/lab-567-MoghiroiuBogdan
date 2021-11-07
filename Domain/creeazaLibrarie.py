def creeaza_librarie(id, titlu, gen, pret, tipReducere):
    '''
    creeaza o carte
    :param id:strig
    :param titlu:string
    :param gen:string
    :param pret:float
    :param tipReducere:string
    :return:o vanzare
    '''

    return {
        "id": id,
        "titlu": titlu,
        "gen": gen,
        "pret": pret,
        "tipReducere": tipReducere

    }


    #carte = [id,titlu,gen,pret,tipReducere]
    #return carte


def getId(librarie):
    '''
    getter pt id
    :param librarie:
    :return:id ul
    '''
    return librarie["id"]
    #return librarie[0]


def getTitlu(librarie):
    '''
    getter pt titlu
    :param librarire:
    :return: titlu
    '''
    return librarie["titlu"]
    #return librarie[1]


def getGen(librarie):
    '''
    getter pt gen
    :param librarie:
    :return: gen
    '''
    return librarie["gen"]
    #return librarie[2]


def getPret(librarie):
    '''
    getter pt pret
    :param librarie:
    :return: pret
    '''
    return librarie["pret"]
    #return librarie[3]

def getTipReducere(librarie):
    '''
    getter pt reducere
    :param librarie:
    :return: reducere
    '''
    return librarie["tipReducere"]
    #return librarie[4]


def toString(librarie):
    return "id: {}, titlu:{}, gen:{}, pret:{}, tipReducere:{}".format(
        getId(librarie),
        getTitlu(librarie),
        getGen(librarie),
        getPret(librarie),
        getTipReducere(librarie),
    )
