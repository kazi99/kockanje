from model import Kockanje, ENA, DVA, TRI, STIRI, PET, SEST, TRIP, QUAD, FULL, ZAP4, ZAP5, YAHT, CHNC, STEVILO_METOV, ZACETEK, KOCKA, lepsa_tabela, TABELA

igralec = Kockanje(poteze=3)

def začetni_meni():
    print('Dobordošli v kockanju!')
    print('Želiš začeti?')
    izbira = input('(Y/N) >> ')
    if izbira.upper() == 'Y':
        baza()
    else:
        baza()

def vpisovanje(kombinacija):
    if igralec.preveri_vpisovanje(kombinacija):
        igralec.vpisovanje_v_tabelo(kombinacija)
        igralec.naslednja_poteza()
        #igralec.trenutni_met = [0,0,0,0,0] # zaenkrat edini nacin, ki ga poznam, kako resetirati kocke pred zacetkom naslednje poteze
        baza()
    else:
        print('\x1b[0;31;5m' + 'Ta kombinacija je že vpisana, izberi drugo.'.upper() + '\x1b[0m')
        baza()

def prvi_met():
    izbira = input('   Pritisni [enter] za met kock ')
    if izbira == '':
        igralec.vrzi()
        igralec.naslednji_met()
        baza()
    else:
        baza()

def vmesni_met():
    print('Če želiš vpisati svoj met, napiši ime kombinacije, sicer napiši indekse kock, ki jih želiš ponovno vreči. ')
    izbira = input('>> ').capitalize()
    if izbira in igralec.odprte_kombinacije:
        vpisovanje(izbira)
    else:
        igralec.vrzi(izbira)
        igralec.naslednji_met()
        baza()

def zadnji_met():
    izbira = input('Pod katero kombinacijo želiš vpisati svoj met? >> ').capitalize()
    if izbira in igralec.odprte_kombinacije:
        vpisovanje(izbira)
    else:
        print('To ni veljavna kombinacija, poskusi še enkrat.')
        metanje()


def metanje():
    if igralec.preostanek_metov == STEVILO_METOV:
        prvi_met()

    elif igralec.preostanek_metov < STEVILO_METOV and igralec.preostanek_metov != 0:
        vmesni_met()
        
    else:
        zadnji_met()

def osnovna_tabela():
    print('Tvoj listek: ')
    print('====================================')
    print('           Enke |  {}  |'.format(lepsa_tabela(igralec.tabela[ENA])))
    print('         Dvojke |  {}  |'.format(lepsa_tabela(igralec.tabela[DVA])))
    print('         Trojke |  {}  |'.format(lepsa_tabela(igralec.tabela[TRI])))
    print('         Štirke |  {}  |'.format(lepsa_tabela(igralec.tabela[STIRI])))
    print('          Petke |  {}  |'.format(lepsa_tabela(igralec.tabela[PET])))
    print('         Šestke |  {}  |'.format(lepsa_tabela(igralec.tabela[SEST])))
    print('________________________\n')
    print('      Tri enake |  {}  |'.format(lepsa_tabela(igralec.tabela[TRIP])))
    print('    Štiri enake |  {}  |'.format(lepsa_tabela(igralec.tabela[QUAD])))
    print('           Full |  {}  |'.format(lepsa_tabela(igralec.tabela[FULL])))
    print('Štiri zaporedne |  {}  |'.format(lepsa_tabela(igralec.tabela[ZAP4])))
    print(' Pet zaporednih |  {}  |'.format(lepsa_tabela(igralec.tabela[ZAP5])))
    print('        Yahtzee |  {}  |     Skupaj'.format(lepsa_tabela(igralec.tabela[YAHT])))
    print('         Chance |  {}  |         {}'.format(lepsa_tabela(igralec.tabela[CHNC]), lepsa_tabela(igralec.skupni_sestevek())))
    print('====================================')
    print('    Tvoj trenutni met')
    print('    A | B | C | D | E    ')
    print('    {} | {} | {} | {} | {}\n'.format(igralec.trenutni_met[0], igralec.trenutni_met[1], igralec.trenutni_met[2], igralec.trenutni_met[3], igralec.trenutni_met[4]))
    print('Na voljo imaš še {} {} in {} {}.'.format(igralec.preostanek_metov, igralec.met_lepo(), igralec.poteze, igralec.poteza_lepo()))
    print('====================================\n')
    metanje()

def konec():
    print('====================================')
    print('             ČESTITKE               ')
    print('    Tvoje skupno število točk je:   ')
    print('                {}                  '.format(lepsa_tabela(igralec.skupni_sestevek())))
    print('====================================')
    izbira = input('     Za izhod pritisni [enter]')
    if izbira == '':
        igralec.reset()
        igralec.tabela = TABELA
        začetni_meni()
    else:
        konec()

def baza():
    if not igralec.konec_kockanja():
        osnovna_tabela()
    else:
        konec()

def kockanje():
    while True:
        začetni_meni()

kockanje()

# zakaj ne vrže vseh kock če ne napišem nič ///
# zakaj se v tabeli ob začetku nove poteze ne resetirajo kocke nazaj na ZACETEK ///

# napiši funkcije ki ujemajo met in poteza z ustreznimi števnostmi