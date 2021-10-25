from Domain.creeazaLibrarie import creeaza_librarie, getTitlu, getId, getGen, getPret, getTipReducere
from logic.CRUD import adauga_carte, stergere_carte, get_by_id


def test_adauga():
    lista = []
    lista = adauga_carte("1", "moara cu noroc", "istoric", 200, "silver", lista)

    assert getId(get_by_id("1",lista)) == "1"
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
    assert get_by_id("2", l)is not None
