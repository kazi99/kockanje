import bottle
from model import Kockanje, ENA, DVA, TRI, STIRI, PET, SEST, TRIP, QUAD, FULL, ZAP4, ZAP5, YAHT, CHNC, STEVILO_METOV, ZACETEK, KOCKA, lepsa_tabela, TABELA, KOMBINACIJE, ST_POTEZ

igralec = Kockanje()

@bottle.get('/')
def osnovna_stran():
    tabela = igralec.tabela
    odprte_kombinacije = igralec.odprte_kombinacije
    st_metov = igralec.preostanek_metov
    met = igralec.trenutni_met
    konec = igralec.konec_kockanja()
    return bottle.template('kockanje_izgled.tpl', tabela=tabela, odprte_kombinacije=odprte_kombinacije, st_metov=st_metov, STEVILO_METOV = STEVILO_METOV, met=met, ZACETEK=ZACETEK, konec=konec)

@bottle.post('/izberi-met/')
def izberi_met():
    if igralec.preostanek_metov == STEVILO_METOV:
        igralec.vrzi()
        igralec.naslednji_met()
        bottle.redirect('/')
    elif igralec.preostanek_metov < STEVILO_METOV:
        a = bottle.request.forms.get('a')
        b = bottle.request.forms.get('b')
        c = bottle.request.forms.get('c')
        d = bottle.request.forms.get('d')
        e = bottle.request.forms.get('e')
        niz = ''
        sez = [a, b, c, d, e]
        imena = 'ABCDE'
        for i in range(5):
            if sez[i] != None:
                niz += imena[i]        
        igralec.vrzi(niz)
        igralec.naslednji_met()
        bottle.redirect('/')

@bottle.post('/izberi-kombinacjo/0/')
def ena():      
    igralec.vpisovanje_v_tabelo(ENA)
    igralec.naslednja_poteza()
    bottle.redirect('/')

@bottle.post('/izberi-kombinacjo/1/')
def dva():
    igralec.vpisovanje_v_tabelo(DVA)
    igralec.naslednja_poteza()
    bottle.redirect('/')

@bottle.post('/izberi-kombinacjo/2/')
def tri():       
    igralec.vpisovanje_v_tabelo(TRI)
    igralec.naslednja_poteza()
    bottle.redirect('/')

@bottle.post('/izberi-kombinacjo/3/')
def stiri():       
    igralec.vpisovanje_v_tabelo(STIRI)
    igralec.naslednja_poteza()
    bottle.redirect('/')

@bottle.post('/izberi-kombinacjo/4/')
def pet():       
    igralec.vpisovanje_v_tabelo(PET)
    igralec.naslednja_poteza()
    bottle.redirect('/')

@bottle.post('/izberi-kombinacjo/5/')
def sest():       
    igralec.vpisovanje_v_tabelo(SEST)
    igralec.naslednja_poteza()
    bottle.redirect('/')

@bottle.post('/izberi-kombinacjo/6/')
def trip():       
    igralec.vpisovanje_v_tabelo(TRIP)
    igralec.naslednja_poteza()
    bottle.redirect('/')

@bottle.post('/izberi-kombinacjo/7/')
def quad():       
    igralec.vpisovanje_v_tabelo(QUAD)
    igralec.naslednja_poteza()
    bottle.redirect('/')

@bottle.post('/izberi-kombinacjo/8/')
def full():       
    igralec.vpisovanje_v_tabelo(FULL)
    igralec.naslednja_poteza()
    bottle.redirect('/')

@bottle.post('/izberi-kombinacjo/9/')
def zap4():       
    igralec.vpisovanje_v_tabelo(ZAP4)
    igralec.naslednja_poteza()
    bottle.redirect('/')

@bottle.post('/izberi-kombinacjo/10/')
def zap5():       
    igralec.vpisovanje_v_tabelo(ZAP5)
    igralec.naslednja_poteza()
    bottle.redirect('/')

@bottle.post('/izberi-kombinacjo/11/')
def yaht():       
    igralec.vpisovanje_v_tabelo(YAHT)
    igralec.naslednja_poteza()
    bottle.redirect('/')
    
@bottle.post('/izberi-kombinacjo/12/')
def chnc():       
    igralec.vpisovanje_v_tabelo(CHNC)
    igralec.naslednja_poteza()
    bottle.redirect('/')

@bottle.get('/reset/')
def resetiraj():
    igralec.reset()
    bottle.redirect('/')    

bottle.run(debug=True, reloader=True)
