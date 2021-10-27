from Logic.crud import add_rezervare
from UserInterface.console import run_console


def main():
    lst_rezervari = []
    add_rezervare(lst_rezervari, '1', 'Georgescu', 'economy', 150, 'da')
    add_rezervare(lst_rezervari, '2', 'Ionescu', 'business', 450, 'da')
    add_rezervare(lst_rezervari, '3', 'Popescu', 'business', 555, 'da')
    add_rezervare(lst_rezervari, '4', 'Popa', 'economy plus', 300, 'nu')
    add_rezervare(lst_rezervari, '5', 'Barbu', 'economy', 180, 'da')
    add_rezervare(lst_rezervari, '6', 'Ion', 'economy', 155, 'nu')
    add_rezervare(lst_rezervari, '7', 'Marin', 'business', 480, 'nu')
    add_rezervare(lst_rezervari, '8', 'Dobrin', 'economy plus', 333, 'da')
    add_rezervare(lst_rezervari, '9', 'Serban', 'economy plus', 295, 'nu')
    add_rezervare(lst_rezervari, '10', 'Ion', 'economy', 210, 'da')


    run_console(lst_rezervari)

main()