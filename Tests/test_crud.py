from Domain.rezervare import creeaza_rezervare, get_id, get_nume, get_clasa, get_pret, get_checkin
from Logic.crud import add_rezervare, delete_rezervare, get_by_id, update_rezervare


def test_add_rezervare():
    lst_rezervari = []

    r1 = creeaza_rezervare(3, 'r1', 'economy', 480, 'da')
    add_rezervare(lst_rezervari, 3, 'r1', 'economy', 480, 'da')
    assert len(lst_rezervari) == 1
    assert get_by_id(lst_rezervari, 3) == r1

    r2 = creeaza_rezervare(5, 'r2', 'economy plus', 500, 'da')
    add_rezervare(lst_rezervari, 5, 'r2', 'economy plus', 500, 'da')
    assert len(lst_rezervari) == 2
    assert get_by_id(lst_rezervari, 3) == r1
    assert get_by_id(lst_rezervari, 5) == r2


def test_delete_rezervare():
    lst_rezervari = []

    add_rezervare(lst_rezervari, 3, 'r1', 'economy', 480, 'da')
    add_rezervare(lst_rezervari, 5, 'r2', 'economy plus', 500, 'da')

    result = delete_rezervare(lst_rezervari, 3)
    assert get_id(get_by_id(result, 5)) == 5
    assert get_by_id(result, 3) is None


def test_update_rezervare():
    r1 = creeaza_rezervare(3, 'r1', 'economy', 480, 'da')
    r2 = creeaza_rezervare(5, 'r2', 'economy plus', 500, 'da')
    lst_rezervari = [r1, r2]
    lst_rezervari = update_rezervare(lst_rezervari, 3, '', 'business', 550, '')
    rezervare_modificata = get_by_id(lst_rezervari, 3)
    assert get_nume(rezervare_modificata) == 'r1'
    assert get_clasa(rezervare_modificata) == 'business'
    assert get_pret(rezervare_modificata) == 550
    assert get_checkin(rezervare_modificata) == 'da'
    assert get_by_id(lst_rezervari, 5) == r2
