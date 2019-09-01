from model import Kockanje, ENA, DVA, TRI, STIRI, PET, SEST, TRIP, QUAD, FULL, ZAP4, ZAP5, YAHT, CHNC, STEVILO_METOV


igralec = Kockanje(poteze=3)

def začetni_meni():
    print('Dobordošli v kockanju!')
    print('Želiš začeti?')
    izbira = input('(Y/N) >> ')
    if izbira == 'Y':
        osnovna_tabela()
    else:
        osnovna_tabela()

def vpisovanje(kombinacija):
    igralec.vpisovanje_v_tabelo(kombinacija)
    igralec.naslednja_poteza()
    osnovna_tabela()

def metanje():
    if igralec.preostanek_metov == STEVILO_METOV:
        izbira = input('Pritisni [enter] za met kock >> ')
        if izbira == '':
            igralec.vrzi()
            igralec.naslednji_met()
            osnovna_tabela()
        else:
            osnovna_tabela ()
    
    elif igralec.preostanek_metov < STEVILO_METOV and igralec.preostanek_metov != 0:
        print('Če želiš vpisati svoj met, napiši ime kombinacije, sicer napiši indekse kock, ki jih želiš ponovno vreči. ')
        izbira = input('>> ')
        if izbira in igralec.odprte_kombinacije:
            vpisovanje(izbira)
        else:
            igralec.vrzi(izbira)
            igralec.naslednji_met()
            osnovna_tabela()

    else:
        izbira = input('Pod katero kombinacijo želiš vpisati svoj met? >> ')
        vpisovanje(izbira)

def osnovna_tabela():
    print('Tvoj listek: ')
    print('========================')
    print('           Enke | {} |'.format(igralec.tabela[ENA]))
    print('         Dvojke | {} |'.format(igralec.tabela[DVA]))
    print('         Trojke | {} |'.format(igralec.tabela[TRI]))
    print('         Štirke | {} |'.format(igralec.tabela[STIRI]))
    print('          Petke | {} |'.format(igralec.tabela[PET]))
    print('         Šestke | {} |'.format(igralec.tabela[SEST]))
    print('________________________\n')
    print('      Tri enake | {} |'.format(igralec.tabela[TRIP]))
    print('    Štiri enake | {} |'.format(igralec.tabela[QUAD]))
    print('           Full | {} |'.format(igralec.tabela[FULL]))
    print('Štiri zaporedne | {} |'.format(igralec.tabela[ZAP4]))
    print(' Pet zaporednih | {} |'.format(igralec.tabela[ZAP5]))
    print('        Yahtzee | {} |'.format(igralec.tabela[YAHT]))
    print('         Chance | {} |'.format(igralec.tabela[CHNC]))
    print('========================')
    print('    Tvoj trenutni met')
    print('    A | B | C | D | E    ')
    print('    {} | {} | {} | {} | {}\n'.format(igralec.trenutni_met[0], igralec.trenutni_met[1], igralec.trenutni_met[2], igralec.trenutni_met[3], igralec.trenutni_met[4]))
    print('Na voljo imaš še {} metov in {} potez.'.format(igralec.preostanek_metov, igralec.poteze))
    print('========================\n')
    metanje()

def main():
    while True:
        začetni_meni()

main()
