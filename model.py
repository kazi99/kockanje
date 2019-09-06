A = 0
B = 1
C = 2
D = 3
E = 4

ENA = 'Enke'
DVA = 'Dvojke'
TRI = 'Trojke'
STIRI = 'Štirke'
PET = 'Petke'
SEST = 'Šestke'
TRIP = 'Tri enake'
QUAD = 'Štiri enake'
FULL = 'Full'
ZAP4 = 'Štiri zaporedne'
ZAP5 = 'Pet zaporednih'
YAHT = 'Yahtzee'
CHNC = 'Chance'

KOCKA = [1, 2, 3, 4, 5, 6]
ZACETEK = [0 for _ in range(5)]

STEVILO_METOV = 3

TABELA = {ENA: None, DVA: None, TRI: None, STIRI: None, PET: None, SEST: None, TRIP: None, QUAD: None, FULL: None, ZAP4: None, ZAP5: None, YAHT: None, CHNC: None}

KOMBINACIJE = [key for key in TABELA]

ST_POTEZ = 13

import random

#-----------------------------Preverjanje kombinacij----------------------------------------

# kombinacij iz zgornje polovice ne bom preverjal, ker si jih lahko kadarkoli vpišeš, njhova vrednost bo samo skupno število pojavitev željenega simbola

def n_enake(met, n):            #pokrije TRIP, QUAD, YAHT
    for simbol in met:
        if met.count(simbol) >= n:
            return True
    return False

def full(met):
    for simbol in met:
        if met.count(simbol) == 3:
            if len(list(set([st for st in met if st != simbol]))) == 1:
                return True
    return False

def stiri_zaporedne(met):       
    mn = set(met)
    return {1,2,3,4}.issubset(mn) or {2,3,4,5}.issubset(mn) or {3,4,5,6}.issubset(mn)

def pet_zaporednih(met):
    mn = set(met)
    return {1,2,3,4,5}.issubset(mn) or {2,3,4,5,6}.issubset(mn)

#-------------------------------------------------------------------------------------------

class Kockanje:

    def __init__(self, poteze=ST_POTEZ, preostanek_metov=STEVILO_METOV):
        self.tabela = dict(TABELA)
        self.trenutni_met = [i for i in ZACETEK]
        self.odprte_kombinacije = KOMBINACIJE.copy()
        self.poteze = poteze
        self.preostanek_metov = preostanek_metov

    def naslednji_met(self):
        if self.preostanek_metov > 0:
            self.preostanek_metov -= 1
        else:
            self.trenutni_met = ZACETEK.copy()

    def naslednja_poteza(self):
            if self.poteze > 0:
                self.poteze -= 1
                self.preostanek_metov = STEVILO_METOV
                self.trenutni_met = ZACETEK.copy()
            else:
                assert False

    def vrzi(self, izbira='ABCDE'):
        if self.preostanek_metov == STEVILO_METOV or izbira == '':
            for i in range(5):
                self.trenutni_met[i] = random.choice(KOCKA)
            self.naslednji_met()

        elif self.preostanek_metov > 0:
            if izbira != 'ABCDE':
                izbira = izbira.upper()
                izbira = list(set(list(izbira)))

            for i in izbira:
                if i in 'ABCDE':
                    self.trenutni_met[eval(i)] = random.choice(KOCKA)     
            self.naslednji_met()
    

    # def preveri_tabelo(self, ime_kombinacije):  
    #     """Preveri ali je kombinacija še odprta v tabeli"""

    #     if ime_kombinacije not in self.odprte_kombinacije:
    #         return False
    #     else:
    #         self.odprte_kombinacije.remove(ime_kombinacije)
    #         return True

    def preveri_kombinacijo(self, ime_kombinacije): 
        """Preveri ali kombinacija v metu ustreza imenu kombinacje v tabeli"""

        met = self.trenutni_met
        if ime_kombinacije == ENA:
            return True
        if ime_kombinacije == DVA:
            return True
        if ime_kombinacije == TRI:
            return True
        if ime_kombinacije == STIRI:
            return True
        if ime_kombinacije == PET:
            return True
        if ime_kombinacije == SEST:
            return True
        if ime_kombinacije == CHNC:
            return True
        if ime_kombinacije == TRIP: 
            return n_enake(met, 3)
        if ime_kombinacije == QUAD:
            return n_enake(met, 4)
        if ime_kombinacije == YAHT:
            return n_enake(met, 5)
        if ime_kombinacije == FULL:
            return full(met)
        if ime_kombinacije == ZAP4:
            return stiri_zaporedne(met)
        if ime_kombinacije == ZAP5:
            return pet_zaporednih(met)


    def tockovanje(self, ime_kombinacije):   
        """Izračuna ustrezen rezultat za dano kombinacijo in jo vpiše v tabelo"""
        
        met = self.trenutni_met
        if ime_kombinacije in [ENA, DVA, TRI, STIRI, PET, SEST]:
            if ime_kombinacije == ENA: i = 1
            elif ime_kombinacije == DVA: i = 2
            elif ime_kombinacije == TRI: i = 3
            elif ime_kombinacije == STIRI: i = 4
            elif ime_kombinacije == PET: i = 5
            elif ime_kombinacije == SEST: i = 6
            self.tabela[ime_kombinacije] = met.count(i) * i

        elif ime_kombinacije in [TRIP, QUAD, CHNC]:
            self.tabela[ime_kombinacije] = sum(met)

        elif ime_kombinacije == FULL:
            self.tabela[ime_kombinacije] = 25
            
        elif ime_kombinacije == ZAP4:
            self.tabela[ime_kombinacije] = 30

        elif ime_kombinacije == ZAP5:
            self.tabela[ime_kombinacije] = 40

        elif ime_kombinacije == YAHT:
            self.tabela[ime_kombinacije] = 50

    def preveri_vpisovanje(self, ime_kombinacije):
        """Prepreči da bi določeno kombinacjo še enkrat vpisal v tabelo."""
        return self.tabela[ime_kombinacije] == None
            
    def vpisovanje_v_tabelo(self, ime_kombinacije):
        if self.preveri_kombinacijo(ime_kombinacije):
            self.tockovanje(ime_kombinacije)
            self.odprte_kombinacije.remove(ime_kombinacije)
            self.naslednja_poteza()
        else:
            self.tabela[ime_kombinacije] = 0
            self.odprte_kombinacije.remove(ime_kombinacije)
            self.naslednja_poteza()

    def postavi_kocke_na_zacetek(self):
        self.trenutni_met = ZACETEK.copy()

    def skupni_sestevek(self):
        sestevek = 0
        for key in self.tabela:
            if self.tabela[key] != None:
                sestevek += self.tabela[key]
        return sestevek

    # def konec_kockanja(self):
    #     for key in self.tabela:
    #         if self.tabela[key] == None:
    #             return False
    #     return True

    def konec_kockanja(self):
        return self.poteze <= 0

    def met_lepo(self):
        if self.preostanek_metov == 3:
            return 'mete'
        elif self.preostanek_metov == 2:
            return 'meta'
        elif self.preostanek_metov == 1:
            return 'met'
        else:
            return 'metov'

    def poteza_lepo(self):
        if self.poteze == 1:
            return 'potezo'
        elif self.poteze == 2:
            return 'potezi'
        elif self.poteze == 3 or self.poteze == 4:
            return 'poteze'
        else:
            return 'potez'

    def reset(self):
        self.tabela = TABELA.copy()
        self.poteze = ST_POTEZ
        self.preostanek_metov = STEVILO_METOV
        self.trenutni_met = ZACETEK.copy()
        self.odprte_kombinacije = KOMBINACIJE.copy()


def lepsa_tabela(x):
        if x == None:
            return '  '
        elif len(str(x)) == 1:
            return ' ' + str(x)
        else:
            return x