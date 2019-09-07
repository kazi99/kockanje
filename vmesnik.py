from model import Kockanje, ENA, DVA, TRI, STIRI, PET, SEST, TRIP, QUAD, FULL, ZAP4, ZAP5, YAHT, CHNC, STEVILO_METOV, ZACETEK, KOCKA, lepsa_tabela, TABELA, KOMBINACIJE

igralec = Kockanje(poteze=3)

def zacetni_meni():
    print('\x1b[0;34;5m' + 'Predlagam ti, da terminal odpreš vsaj do te višine.' + '\x1b[0m')
    print('')
    print('====================================')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('      Dobrodošli v kockanju!')
    print('          Želiš začeti?  ')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('====================================\n')
    print('(Y/N)')
    izbira = input('>> ')
    if izbira.upper() == 'Y':
        baza()
    else:
        zacetni_meni()

def vpisovanje(kombinacija):
    if igralec.preveri_vpisovanje(kombinacija):
        igralec.vpisovanje_v_tabelo(kombinacija)
        baza()
    else:
        print('\x1b[0;31;5m' + 'Kombinacija {} je že vpisana, izberi drugo.'.format(kombinacija) + '\x1b[0m')
        baza()

def prvi_met():
    izbira = input('   Pritisni [enter] za met kock \n')
    if izbira == '':
        igralec.vrzi()
        baza()
    else:
        baza()

def vmesni_met():
    print('Če želiš vpisati svoj met, napiši ime kombinacije, sicer napiši indekse kock, ki jih želiš ponovno vreči. ')
    izbira = input('>> ').capitalize()
    if izbira in KOMBINACIJE:
        vpisovanje(izbira)
    else:
        igralec.vrzi(izbira)
        baza()

def zadnji_met():
    print('Pod katero kombinacijo želiš vpisati svoj met?')
    izbira = input('>> ').capitalize()
    if izbira in igralec.odprte_kombinacije:
        vpisovanje(izbira)
    else:
        print('\x1b[0;31;5m' + 'To ni veljavna kombinacija, poskusi še enkrat.' + '\x1b[0m')
        baza()


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
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('             ČESTITKE               ')
    print('    Tvoje skupno število točk je:   ')
    print('                {}                  '.format(lepsa_tabela(igralec.skupni_sestevek())))
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('====================================\n')
    izbira = input('     Za izhod pritisni [enter]\n')
    if izbira == '':
        igralec.reset()
        zacetni_meni()
    else:
        konec()

def baza():
    if not igralec.konec_kockanja():
        osnovna_tabela()
    else:
        konec()

def kockanje():
    while True:
        zacetni_meni()

kockanje()