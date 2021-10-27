from Domain.rezervare import get_str, get_pret
from Logic.crud import get_by_id, add_rezervare, delete_rezervare, update_rezervare
from Logic.operatiuni import trecerea_rezervarilor_la_clasa_superioara, ieftinire_rezervare, \
    get_rezervare_pret_maxim_pe_clasa


def print_menu():
    print('1. CRUD - Create, Read, Update, Delete')
    print('2. Operațiuni')
    print('x. Ieșire')


def run_crud(lst_rezervari):

    def handle_adaugare(lst_rezervari):
        try:
            id_rezervare = input('Dați id-ul: ')
            rezervare_existenta = get_by_id(lst_rezervari, id_rezervare)
            if rezervare_existenta is not None:
                raise ValueError('ID-ul există deja!')
            nume = input('Dați numele: ')
            clasa = input('Dați clasa: ')
            pret = float(input('Dați prețul: '))
            checkin = input('Checkin: ')
            add_rezervare(lst_rezervari, id_rezervare, nume, clasa, pret, checkin)
            print('Rezervarea a fost adăugată!')
        except ValueError as ve:
            print('Eroare:', ve, 'Reîncearcă!')

    def handle_stergere(lst_rezervari):
        try:
            id_rezervare = input('Dați id-ul de șters: ')
            lst_rezervari = delete_rezervare(lst_rezervari, id_rezervare)
            print('Rezervarea a fost ștearsă!')
            return lst_rezervari
        except ValueError as ve:
            print('Eroare:', ve, 'Reîncearcă!')
        return lst_rezervari

    def handle_modificare(lst_rezervari):
        try:
            id_rezervare = input('Dați id-ul de modificat: ')
            rezervare_existenta = get_by_id(lst_rezervari, id_rezervare)
            if rezervare_existenta is None:
                raise ValueError('ID-ul dat nu există!')
            nume = input('Dați numele (lăsați gol pentru a nu se modifica): ')
            clasa = input('Dați clasa (lăsați gol pentru a nu se modifica): ')
            pret = input('Dați prețul (lăsați gol pentru a nu se modifica): ')
            checkin = input('Checkin (lăsați gol pentru a nu se modifica): ')
            return update_rezervare(lst_rezervari, id_rezervare, nume, clasa, pret, checkin)
        except ValueError as ve:
            print('Eroare:', ve, 'Reîncearcă!')
            return lst_rezervari

    def handle_show_all(lst_rezervari):
        for rezervare in lst_rezervari:
            print(get_str(rezervare))

    while True:
        print('1. Adăugare')
        print('2. Ștergere')
        print('3. Modificare')
        print('a. Afișare toate')
        print('b. Back')
        op = input('Alegeți opțiunea: ')
        if op == '1':
            handle_adaugare(lst_rezervari)
        elif op == '2':
            lst_rezervari = handle_stergere(lst_rezervari)
        elif op == '3':
            lst_rezervari = handle_modificare(lst_rezervari)
        elif op == 'a':
            handle_show_all(lst_rezervari)
        elif op == 'b':
            break
        else:
            print('Comandă invalidă, reîncearcă!')
        print()
    return lst_rezervari

def run_operatiuni(lst_rezervari):

    def handle_clasa_superioara(lst_rezervari):
        nume = input('Dați numele: ')
        trecerea_rezervarilor_la_clasa_superioara(lst_rezervari, nume)
        print('Rezervările făcute pe numele', nume, 'au fost trecute la o clasă superioară.')

    def handle_ieftinire_rezervari(lst_rezervari):
        try:
            procentaj = input('Dați procentajul cu care să se ieftinească rezervarea: ')
            if not(int(procentaj) > 0) or not(int(procentaj) < 100):
                raise ValueError('Procentajul trebuie să fie cuprins între 0 și 100!')
            ieftinire_rezervare(lst_rezervari, procentaj)
        except ValueError as ve:
            print('Eroare:', ve, 'Reîncearcă!')

    def handle_pret_max_pe_clasa(lst_rezervari):
        rezultat = get_rezervare_pret_maxim_pe_clasa(lst_rezervari)
        for clasa in rezultat:
            print('Cel mai mare preț de la clasa {} este: {}'.format(clasa, get_pret(rezultat[clasa])))

    while True:
        print('1. Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară.')
        print('2. Ieftinirea tuturor rezervărilor la care s-a făcut checkin.')
        print('3. Determinarea prețului maxim pentru fiecare clasă.')
        print('4. Ordonarea rezervărilor descrescător după preț.')
        print('5. Afișarea sumelor prețurilor pentru fiecare nume.')
        print('b. Back')
        op = input('Alegeți opțiunea: ')
        if op == '1':
            handle_clasa_superioara(lst_rezervari)
        elif op == '2':
            handle_ieftinire_rezervari(lst_rezervari)
        elif op == '3':
            handle_pret_max_pe_clasa(lst_rezervari)
        elif op == '4':
            pass
        elif op == '5':
            pass
        elif op == 'b':
            break
        else:
            print('Comandă invalidă, reîncearcă!')
        print()


def run_console(lst_rezervari):
    while True:
        print_menu()
        op = input('Alegeți opțiunea: ')
        if op == '1':
            run_crud(lst_rezervari)
        elif op == '2':
            run_operatiuni(lst_rezervari)
        elif op == 'x':
            break
        else:
            print('Comandă invalidă')
    return lst_rezervari