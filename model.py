A = 0
B = 1
C = 2
D = 3
E = 4

KOCKA = [1, 2, 3, 4, 5, 6]
ZACETEK = [0 for _ in range(len(KOCKA) - 1)]

STEVILO_METOV = 3

TABELA = {'Enke': None, 'Dvojke': None, 'Trojke': None, 'Štirke': None, 'Petke': None, 'Šestke': None, 'Tri enake': None, 'Štiri enake': None, 'Full': None, 'Zaporedje štirih zaporednih': None, 'Zaporedje petih zaporednih': None, 'Yahtzee': None, 'Chance': None}

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

class metanje:

    def __init__(self, met=ZACETEK, preostanek_metov=STEVILO_METOV): 
        self.met = met
        self.preostanek_metov = preostanek_metov


    def vrzi(self, izbira='ABCDE'):
        if self.preostanek_metov > 0:

            if izbira != 'ABCDE':
                izbira = izbira.upper()
                izbira = list(set(list(izbira)))

            for i in izbira:
                if i in 'ABCDE':
                    self.met[eval(i)]= random.choice(KOCKA)

            self.preostanek_metov -= 1        
            return self.met

        else:
            return self.met

class kockanje:

    def __init__(self, tabela=TABELA, poteze=ST_POTEZ):
        self.tabela = tabela
        self.poteze = poteze

    def naslednja_poteza(self):
        if self.poteze > 0:
            self.poteze -= 1
            return metanje()
        else:
            return None

#    def tockovanje(self, kombinacija):
