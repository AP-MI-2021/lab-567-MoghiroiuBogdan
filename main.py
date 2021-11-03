from UI.console import menu
from UI.console_2 import MENU
from tests.testALl import test_all


def main():
    test_all()
    print("1.consola veche")
    print("2.consola noua")
    console=int(input("dati nr consolei pe care vreti sa o alegeti"))
    if console == 1:
        menu([])
    elif console == 2:
        MENU([])

if __name__ == '__main__':
    main()