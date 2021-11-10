from Domain.creeazaLibrarie import getId
from logic.CRUD import adauga_carte


def test_undo_redo():
    l = []
    undoList = []
    redoList = []

    undoList.append(l)
    redoList.clear()

    l = adauga_carte("1", "moara cu noroc", "istoric", 100, "gold", l)

    undoList.append(l)
    redoList.clear()

    assert (l) == [{'id': '1', 'titlu': 'moara cu noroc', 'gen': 'istoric', 'pret': 100, 'tipReducere': 'gold'}]

    l = adauga_carte("2", "moara cu noroc", "istoric", 100, "gold", l)

    undoList.append(l)
    redoList.clear()

    l = adauga_carte("3", "moara cu noroc", "istoric", 100, "gold", l)

    assert (l) == [{'id': '1', 'titlu': 'moara cu noroc', 'gen': 'istoric', 'pret': 100, 'tipReducere': 'gold'},
                   {'id': '2', 'titlu': 'moara cu noroc', 'gen': 'istoric', 'pret': 100, 'tipReducere': 'gold'},
                   {'id': '3', 'titlu': 'moara cu noroc', 'gen': 'istoric', 'pret': 100, 'tipReducere': 'gold'}]

    if len(undoList) > 0:
        redoList.append(l)
        l = undoList.pop()

    assert (l) == [{'id': '1', 'titlu': 'moara cu noroc', 'gen': 'istoric', 'pret': 100, 'tipReducere': 'gold'},
                    {'id': '2', 'titlu': 'moara cu noroc', 'gen': 'istoric', 'pret': 100, 'tipReducere': 'gold'}]

    if len(undoList) > 0:
        redoList.append(l)
        l = undoList.pop()
    assert (l) == [{'id': '1', 'titlu': 'moara cu noroc', 'gen': 'istoric', 'pret': 100, 'tipReducere': 'gold'}]

    if len(redoList) > 0:
        undoList.append(l)
        l = redoList.pop()
    assert (l) == [{'id': '1', 'titlu': 'moara cu noroc', 'gen': 'istoric', 'pret': 100, 'tipReducere': 'gold'},
                    {'id': '2', 'titlu': 'moara cu noroc', 'gen': 'istoric', 'pret': 100, 'tipReducere': 'gold'}]

    if len(redoList) > 0:
        undoList.append(l)
        l = redoList.pop()
    assert (l) == [{'id': '1', 'titlu': 'moara cu noroc', 'gen': 'istoric', 'pret': 100, 'tipReducere': 'gold'},
                   {'id': '2', 'titlu': 'moara cu noroc', 'gen': 'istoric', 'pret': 100, 'tipReducere': 'gold'},
                   {'id': '3', 'titlu': 'moara cu noroc', 'gen': 'istoric', 'pret': 100, 'tipReducere': 'gold'}]

