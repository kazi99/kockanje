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
ZAP4 = 'Zaporedje štirih zaporednih'
ZAP5 = 'Zaporedje petih zaporednih'
YAHT = 'Yahtzee'
CHNC = 'Chance'

KOCKA = [1, 2, 3, 4, 5, 6]
ZACETEK = [0 for _ in range(len(KOCKA) - 1)]

STEVILO_METOV = 3

TABELA = {ENA: None, 'Dvojke': None, 'Trojke': None, 'Štirke': None, 'Petke': None, 'Šestke': None, 'Tri enake': None, 'Štiri enake': None, 'Full': None, 'Zaporedje štirih zaporednih': None, 'Zaporedje petih zaporednih': None, 'Yahtzee': None, 'Chance': None}

KOMBINACIJE = [key for key in TABELA]

ST_POTEZ = 13

import random

#-----------------------------Preverjanje kombinacij----------------------------------------

# kombinacij iz zgornje polovice ne bom preverjal, ker si jih lahko kadarkoli vpišeš, njhova vrednost bo samo skupno število pojavitev željenega simbola

def n_enake(met, n):            #pokrije 'Tri enake', 'Štiri enake', 'Yahtzee'
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

    def __init__(self, tabela=TABELA, poteze=ST_POTEZ, preostanek_metov=STEVILO_METOV, trenutni_met=ZACETEK, odprte_kombinacije=KOMBINACIJE):
        self.tabela = tabela
        self.poteze = poteze
        self.preostanek_metov = preostanek_metov
        self.trenutni_met = trenutni_met
        self.odprte_kombinacije = odprte_kombinacije

    def vrzi(self, izbira='ABCDE'):
        if self.preostanek_metov == STEVILO_METOV:
            for i in range(5):
                self.trenutni_met[i] = random.choice(KOCKA)

        if self.preostanek_metov > 0:

            if izbira != 'ABCDE':
                izbira = izbira.upper()
                izbira = list(set(list(izbira)))

            for i in izbira:
                if i in 'ABCDE':
                    self.trenutni_met[eval(i)] = random.choice(KOCKA)     
            
    def naslednji_met(self):
        if self.preostanek_metov > 0:
            self.preostanek_metov -= 1
        else:
            self.trenutni_met = ZACETEK
            self.poteze -= 1
    
    def naslednja_poteza(self):
            if self.poteze > 0:
                self.poteze -= 1
                self.preostanek_metov = STEVILO_METOV
                self.trenutni_met = ZACETEK
            else:
                raise Exception

    def preveri_tabelo(self, ime_kombinacije):  
        """Preveri ali je kombinacija še odprta v tabeli"""

        if ime_kombinacije not in self.odprte_kombinacije:
            return False
        else:
            self.odprte_kombinacije.remove(ime_kombinacije)
            return True

    def preveri_kombinacijo(self, ime_kombinacije): 
        """Preveri ali kombinacija v metu ustreza imenu kombinacje v tabeli"""

        met = self.trenutni_met
        if ime_kombinacije == 'Tri enake': 
            return n_enake(met, 3)
        if ime_kombinacije == 'Štiri enake':
            return n_enake(met, 4)
        if ime_kombinacije == 'Yahtzee':
            return n_enake(met, 5)
        if ime_kombinacije == 'Full':
            return full(met)
        if ime_kombinacije == 'Zaporedje štirih zaporednih':
            return stiri_zaporedne(met)
        if ime_kombinacije == 'Zaporedje petih zaporednih':
            return pet_zaporednih(met)


    def tockovanje(self, ime_kombinacije):   
        """V tabelo zapiše ustrezen rezultat za dano kombinacijo"""
        
        met = self.trenutni_met
        if ime_kombinacije in [ENA, 'Dvojke', 'Trojke', 'Štirke', 'Petke', 'Šestke']:
            if ime_kombinacije == ENA: i = 1
            elif ime_kombinacije == 'Dvojke': i = 2
            elif ime_kombinacije == 'Trojke': i = 3
            elif ime_kombinacije == 'Štirke': i = 4
            elif ime_kombinacije == 'Petke': i = 5
            elif ime_kombinacije == 'Šestke': i = 6
            self.tabela[ime_kombinacije] = met.count(i) * i

        elif ime_kombinacije in ['Tri enake', 'Štiri enake', 'Chance']:
            self.tabela[ime_kombinacije] = sum(met)

        elif ime_kombinacije == 'Full':
            self.tabela[ime_kombinacije] = 25
            
        elif ime_kombinacije == 'Zaporedje štirih zaporednih':
            self.tabela[ime_kombinacije] = 30

        elif ime_kombinacije == 'Zaporedje petih zaporednih':
            self.tabela[ime_kombinacije] = 40

        elif ime_kombinacije == 'Yahtzee':
            self.tabela[ime_kombinacije] = 50

        else:
            self.tabela[ime_kombinacije] = 0

    def konec_kockanja(self):
        for key in self.tabela:
            if self.tabela[key] == None:
                return False
        return True