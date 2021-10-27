from Domain.rezervare import get_nume, get_clasa, set_clasa, get_checkin, get_pret, set_pret


def trecerea_rezervarilor_la_clasa_superioara(lst_rezervari, nume):
    """
    Modifică clasa rezervărilor făcute pe un nume citit de la tastatură (economy -> economy plus -> business).
    :param lst_rezervari: lista inițială cu rezervări
    :param nume: numele rezervărilor care urmează să fie modificate
    :return:
    """
    for rezervare in lst_rezervari:
        if get_nume(rezervare) == nume:
            if get_clasa(rezervare) == 'economy':
                clasa = 'economy plus'
                set_clasa(rezervare, clasa)
            elif get_clasa(rezervare) == 'economy plus':
                clasa = 'business'
                set_clasa(rezervare, clasa)


def ieftinire_rezervare(lst_rezervari, procentaj):
    """
    Ieftinește rezervările la care s-a făcut checkin cu un procentaj citit.
    :param lst_rezervari: lista inițială cu rezervări
    :param procentaj: procentajul cu care se ieftinesc rezervările
    :return:
    :raises: ValueError, dacă procentajul dat nu este cuprins între 0 și 100 sau nu e de tip int
    """
    for rezervare in lst_rezervari:
        if get_checkin(rezervare) == 'da':
            pret = get_pret(rezervare) - int(procentaj) / 100 * get_pret(rezervare)
            set_pret(rezervare, pret)


def get_rezervare_pret_maxim_pe_clasa(lst_rezervari):
    """
    Returnează rezervarea cu cel mai mare preț de la fiecare clasă.
    :param lst_rezervari: lista cu toate rezervările
    :return: un dicționar cu cheile fiind clasele și valorile rezervările cu cel mai mare preț din acea clasă
    """
    result = {}
    for rezervare in lst_rezervari:
        clasa = get_clasa(rezervare)
        if clasa in result:
            if get_pret(rezervare) > get_pret(result[clasa]):
                result[clasa] = rezervare
        else:
            result[clasa] = rezervare
    return result
