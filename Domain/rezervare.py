
def get_id(rezervare):
    '''
    Getter pt id-ul rezervarii
    :param rezervare: rezervarea
    :return:id-ul rezervarii dat ca parametru
    '''
    return rezervare[0]

def get_nume(rezervare):
    '''
    Getter pt numele clientului
    :param rezervare:rezervarea
    :return:numele rezervarii dat ca parametru
    '''
    return rezervare[1]

def get_clasa(rezervare):
    '''
    Getter pt clasa rezervarii
    :param rezervare: rezervarea
    :return:clasa rezervarii dat ca parametru
    '''
    return rezervare[2]

def set_clasa(rezervare, clasa):
    """
    Modifică clasa unei rezervări.
    :param rezervare: rezervarea de modificat
    :param clasa: noua clasă
    :return:
    """
    rezervare[2] = clasa

def get_pret(rezervare):
    '''
    Getter pt pretul rezervarii
    :param rezervare: rezervarea
    :return:pretul rezervarii dat ca parametru
    '''
    return rezervare[3]

def set_pret(rezervare, pret):
    """
    Modifică prețul unei rezervări.
    :param rezervare: rezervarea de modificat
    :param pret: noul preț
    :return:
    """
    rezervare[3] = pret


def get_checkin(rezervare):
    '''
    Getter pt checkinul rezervarii
    :param rezervare: rezervarea
    :return:checkin-ul rezervarii dat ca parametru
    '''
    return rezervare[4]

def get_str(rezervare):
    return f'Rezervarea cu id-ul:{get_id(rezervare)}, numele:{get_nume(rezervare)}, la clasa :{get_clasa(rezervare)},/' \
           f' cu pretul:{get_pret(rezervare)} si checkinul:{get_checkin(rezervare)}'

def creeaza_rezervare(id_rezervare, nume, clasa, pret, checkin):
    '''
    Creeaza o rezervare la o companie aeriana.
    :param id_rezervare: id-ul rezervarii, unic
    :param nume: numele clientului, nenul
    :param clasa: clasa zborului, poate fi economy, economy + sau business
    :param pret: pretul rezervarii
    :param checkin: checkin-ul da sau nu
    :return:
    '''

    obiect = []
    obiect.append(id_rezervare)
    obiect.append(nume)
    obiect.append(clasa)
    obiect.append(float(pret))
    obiect.append(checkin)
    return obiect
