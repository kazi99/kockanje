A = 0
B = 1
C = 2
D = 3
E = 4

KOCKA = [1, 2, 3, 4, 5, 6]
ZACETEK = [0 for _ in range(len(KOCKA) - 1)]

STEVILO_METOV = 3

TABELA = {}

import random

class kockanje:

    def __init__(self, met=ZACETEK): #preostanek_metov=STEVILO_METOV
        self.met = met


    def vrzi(self, izbira='ABCDE'):
        
        if izbira != 'ABCDE':
            izbira = izbira.upper()
            izbira = list(set(list(izbira)))

        for i in izbira:
            if i in 'ABCDE':
                self.met[eval(i)]= random.choice(KOCKA)

