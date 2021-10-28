from Domain.creeazaLibrarie import creeaza_librarie, getTitlu, getId, getGen, getPret, getTipReducere
from logic.CRUD import adauga_carte, stergere_carte, get_by_id
from logic.functionalitati import discount, modifica_genul, pret_minim


def test_adauga():
    lista = []
    lista = adauga_carte("1", "moara cu noroc", "istoric", 200, "silver", lista)

    assert getId(get_by_id("1", lista)) == "1"
    assert getTitlu(get_by_id("1", lista)) == "moara cu noroc"
    assert getGen(get_by_id("1", lista)) == "istoric"
    assert getPret(get_by_id("1", lista)) == 200
    assert getTipReducere(get_by_id("1", lista)) == "silver"


def test_stergere():
    l = []
    l = adauga_carte("1", "moara cu noroc", "istoric", 200, "silver", l)
    l = adauga_carte("2", "enigma otiliei", "romantic", 450, "gold", l)

    l = stergere_carte("1", l)

    assert get_by_id("1", l) is None
    assert get_by_id("2", l) is not None


def test_discount():
    l = []
    l = adauga_carte("1", "moara cu noroc", "istoric", 100, "gold", l)

    l = discount(l)

    assert getPret(l[0]) == 90.0


def test_modif_genul():
    l = []
    l = adauga_carte("1", "moara cu noroc", "istoric", 100, "gold", l)
    l = adauga_carte("2", "moara cu noroc", "istoric", 50, "gold", l)
    l = adauga_carte("3", "moara cu noroc", "istoric", 90, "gold", l)
    l = adauga_carte("4", "moara cu noroc", "istoric", 60, "gold", l)

    l = modifica_genul("moara cu noroc", l, "dramatic")

    assert getGen(l[0]) == "dramatic"


def test_pret_minim():
    l=[]
    l = adauga_carte("1", "moara cu noroc", "istoric", 100, "gold", l)
    l = adauga_carte("2", "moara cu noroc", "istoric", 50, "gold", l)
    l = adauga_carte("3", "moara cu noroc", "istoric", 90, "gold", l)
    l = adauga_carte("4", "moara cu noroc", "istoric", 60, "gold", l)

    l=pret_minim(l)

    assert l["istoric"] == 50
