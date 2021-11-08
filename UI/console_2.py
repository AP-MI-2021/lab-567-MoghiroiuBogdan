from UI.console import show_all
from logic.CRUD import adauga_carte, stergere_carte, modifica_carte


def help():
    '''
    e un nou menu prin care comenzile se separa prin ; si prin ,iar comenzile sunt urm:add
    showall,delete,update
    :return:
    '''
    print("add,id,titlu,gen,pret,tipReducere")
    print("delete,id")
    print("showall")
    print("update,id,titlu,gen,pret,reducere")
    print("stop")


def MENU(lista):

    while True:
            option = input("introduceti comanda: ")

            action = option.split(";")
            for line in action:
                command=line.split(",")
                if command[0] == "help":
                    help()
                elif command[0] == "add":
                    try:
                        lista=adauga_carte(command[1],command[2],command[3],float(command[4]),command[5],lista)
                    except ValueError as ve:
                        print("eroare {}".format(ve))
                elif command[0] == "delete":
                    lista=stergere_carte(command[1],lista)
                elif command[0] == "update":
                    try:
                        lista=modifica_carte(command[1],command[2],command[3],float(command[4]),command[5],lista)
                    except ValueError as ve:
                        print("eroare {}".format(ve))
                elif command[0] == "showall":
                    show_all(lista)
                elif command[0] == "stop":
                    break
                else:
                    print("Comanda introdusa este gresita! Reincercati!")
