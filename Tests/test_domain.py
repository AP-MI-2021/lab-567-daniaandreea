from Domain.rezervare import creeaza_rezervare, get_id, get_nume, get_clasa, get_pret, get_checkin, set_pret, set_clasa


def test_domain():
    r1 = creeaza_rezervare(3, 'r1', 'economy', 480, 'da')
    assert get_id(r1) == 3
    assert get_nume(r1) == 'r1'
    assert get_clasa(r1) == 'economy'
    assert get_pret(r1) == 480
    assert get_checkin(r1) == 'da'
    pret = 500
    set_pret(r1, pret)
    assert get_pret(r1) == 500
    clasa = 'business'
    set_clasa(r1, clasa)
    assert get_clasa(r1) == 'business'
