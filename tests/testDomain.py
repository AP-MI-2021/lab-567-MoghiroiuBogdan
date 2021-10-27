from Domain.creeazaLibrarie import creeaza_librarie, getId, getTitlu, getGen, getPret, getTipReducere


def test_librarie():
    l = creeaza_librarie("1", "moara cu noroc", "istoric", 200, "silver")

    assert getId(l) == "1"
    assert getTitlu(l) == "moara cu noroc"
    assert getGen(l) == "istoric"
    assert getPret(l) == 200
    assert getTipReducere(l) == "silver"