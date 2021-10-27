from Domain.rezervare import get_id, creeaza_rezervare, get_checkin, get_pret, get_clasa, get_nume


def get_by_id(lst_rezervari, id_rezervare):
    """
    Găsește o rezervare după id.
    :param lst_rezervari: lista cu rezervări
    :param id_rezervare: id-ul rezervării căutate
    :return: rezervarea cu id-ul id sau None dacă nu există
    """
    for rezervare in lst_rezervari:
        if get_id(rezervare) == id_rezervare:
            return rezervare
    return None


def add_rezervare(lst_rezervari, id_rezervare, nume, clasa, pret, checkin):
    """
    Adaugă o nouă rezervare.
    :param lst_rezervari: lista curentă de rezervări
    :param id_rezervare: id-ul rezervării
    :param nume: numele
    :param clasa: clasa
    :param pret: prețul
    :param checkin: starea checkin-ului
    :return:

    """

    rezervare = creeaza_rezervare(id_rezervare, nume, clasa, pret, checkin)
    lst_rezervari.append(rezervare)


def delete_rezervare(lst_rezervari, id_rezervare):
    """
    Șterge o rezervare.
    :param lst_rezervari: lista curentă de rezervări
    :param id_rezervare: id-ul rezervării de șters
    :return: o nouă listă din care va lipsi rezervarea cu id-ul id
    :raises: ValueError, dacă ID-ul nu există
    """
    rezervare_existenta = get_by_id(lst_rezervari, id_rezervare)
    if rezervare_existenta is None:
        raise ValueError('ID-ul dat nu există!')
    rezultat = []
    for rezervare in lst_rezervari:
        if get_id(rezervare) != id_rezervare:
            rezultat.append(rezervare)
    return rezultat


def update_rezervare(lst_rezervari, id_de_modificat, nume, clasa, pret, checkin):
    """
    Modifică proprietățile unei rezervări.
    :param lst_rezervari: lista curentă de rezervări
    :param id_de_modificat: id-ul rezervării de modificat
    :param nume: numele
    :param clasa: clasa
    :param pret: prețul
    :param checkin: starea checkin-ului
    :return:
    """
    rezervari_modificate = []
    for rezervare in lst_rezervari:
        if get_id(rezervare) == id_de_modificat:
            rezervare_noua = creeaza_rezervare(
                id_de_modificat,
                nume if nume != '' else get_nume(rezervare),
                clasa if clasa != '' else get_clasa(rezervare),
                float(pret) if pret != '' else get_pret(rezervare),
                checkin if checkin != '' else get_checkin(rezervare),
            )
            rezervari_modificate.append(rezervare_noua)
        else:
            rezervari_modificate.append(rezervare)
    return rezervari_modificate
