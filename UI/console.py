from Domain.creeazaLibrarie import toString
from logic.CRUD import adauga_carte, stergere_carte, modifica_carte
from logic.functionalitati import discount, modifica_genul, pret_minim, ordoneaza_crescator, get_number_of_titles


def ui_adauga_carte(lista, undoList,redoList):
    try:
        id = input("dati id ul:")
        titlu = input("dati titlu:")
        gen = input("dati gen:")
        pret = float(input("dati pretul:"))
        tipReducere = input("dati tipul reducerii:")

        rez = adauga_carte(id, titlu, gen, pret, tipReducere, lista)
        undoList.append(lista)
        redoList.clear()
        return rez

    except ValueError as ve:
        print("eroare {}".format(ve))
        return lista


def ui_sterge_carte(lista, undoList, redoList):
    id = input("dati id ul:")

    rez = stergere_carte(id, lista)
    undoList.append(lista)
    redoList.clear()
    return rez


def ui_modifica_carte(lista, undoList, redoList):
    try:
        id = input("dati id ul cartii care se va modifica:")
        titlu = input("dati noul titlu:")
        gen = input("dati noul gen:")
        pret = float(input("dati noul pretul:"))
        tipReducere = input("dati noul tip de reducere:")

        rez = modifica_carte(id, titlu, gen, pret, tipReducere,lista)
        undoList.append(lista)
        redoList.clear()
        return rez
    except ValueError as ve:
        print("eroare {} ".format(ve))
        return lista



def show_all(lista):
    for carte in lista:
        print(toString(carte))


def ui_discount_carte(lista):

    return discount(lista)


def ui_modifica_genul(lista):
    title = input("dati titlu pt care cartea sa isi modifice genul:")
    noulgen = input("dati noul gen:")

    return modifica_genul(title,lista,noulgen)


def ui_minimul_pret(lista):
    return pret_minim(lista)


def ui_ordoneaza_crescator(lista):
    return ordoneaza_crescator(lista)


def ui_get_number_of_titles(lista):
    return get_number_of_titles(lista)


def menu(lista):
    undoList=[]
    redoList=[]
    while True:
        print("1.adauga cartea:")
        print("2.sterge cartea:")
        print("3.modifica cartea:")
        print("4.reducere de 5% pt silver si de 10% pt gold:")
        print("5.modifica genul dupa un titlu dat:")
        print("6.afiseaza pretul min in fct de gen:")
        print("7.ordoneaza dupa pret:")
        print("8.Afișarea numărului de titluri distincte pentru fiecare gen:")
        print("u.Undo")
        print("r.Redo")
        print("a. afiseaza cartea:")
        print("x. IESIRE")


        option = input("dati numarul:")
        if option == "1":
            lista = ui_adauga_carte(lista, undoList, redoList)
        elif option == "2":
            lista = ui_sterge_carte(lista,undoList, redoList)
        elif option == "3":
            lista = ui_modifica_carte(lista,undoList, redoList)
        elif option=="4":
            lista = ui_discount_carte(lista)
        elif option == "5":
            lista=ui_modifica_genul(lista)
        elif option == "6":
            print(ui_minimul_pret(lista))
        elif option == "7":
            print(ui_ordoneaza_crescator(lista))
        elif option == "8":
            print(ui_get_number_of_titles(lista))
        elif option == "u":
            if len(undoList) > 0:
                redoList.append(lista)
                lista = undoList.pop()
            else:
                print("NU se poate face Undo!")
        elif option == "r":
            if len(redoList) >0:
                undoList.append(lista)
                lista=redoList.pop()
            else:
                print("NU se poate face Redo!")
        elif option == "a":
            show_all(lista)
        elif option == "x":
            break