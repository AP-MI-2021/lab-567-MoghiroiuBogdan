from tests.testCRUD import test_adauga, test_stergere, test_discount, test_modif_genul, test_pret_minim, test_ordonare
from tests.testDomain import test_librarie


def test_all():
    test_librarie()
    test_adauga()
    test_stergere()
    test_discount()
    test_modif_genul()
    test_pret_minim()
    test_ordonare()
