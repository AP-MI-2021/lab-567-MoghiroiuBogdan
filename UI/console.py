from Domain.creeazaLibrarie import toString
from logic.CRUD import adauga_carte, stergere_carte, modifica_carte


def ui_adauga_carte(lista):
    id = input("dati id ul:")
    titlu = input ("dati titlu:")
    gen = input("dati gen:")
    pret = float(input("dati pretul:"))
    tipReducere= input("dati tipul reducerii:")

    return adauga_carte(id, titlu, gen, pret, tipReducere,lista)


def ui_sterge_carte(lista):
    id = input("dati id ul:")

    return stergere_carte(id, lista)


def ui_modifica_carte(lista):
    id = input("dati id ul cartii care se va modifica:")
    titlu = input("dati noul titlu:")
    gen = input("dati noul gen:")
    pret = float(input("dati noul pretul:"))
    tipReducere = input("dati noul tip de reducere:")

    return modifica_carte(id, titlu, gen, pret, tipReducere,lista)


def show_all(lista):
    for carte in lista:
        print(toString(carte))


def menu(lista):

    while True:
        print("1.adauga cartea:")
        print("2.sterge cartea:")
        print("3.modifica cartea")
        print("a. afiseaza cartea")
        print("x. IESIRE")

        option = input("dati numarul:")
        if option == "1":
            lista = ui_adauga_carte(lista)
        elif option == "2":
            lista = ui_sterge_carte(lista)
        elif option == "3":
            lista = ui_modifica_carte(lista)
        elif option == "a":
            show_all(lista)
        elif option == "x":
            break