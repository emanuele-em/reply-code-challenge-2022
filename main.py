import pandas as pd

lista_punteggi = []
lista_punteggi_sorted = []
lista_finale = []

with open('01.txt') as f:
    si,smax,t,d = [int(x) for x in next(f).split()]
    demons = []
    for line in f: # read rest of lines
        demons.append([int(x) for x in line.split()])

def calcola_punteggio_fragment(lista):
    peso = 1
    for frag in lista:
        punteggio =+ frag*peso
        peso += 1
    return punteggio
      

def calcola_punteggio_primi_parametri(sr,tr,sc):
    punteggio = sr/(tr*sc)
    return punteggio

def crea_lista_punteggi(demons):
    i=0
    for demon in demons:
        punteggio = calcola_punteggio_fragment(demon)*calcola_punteggio_primi_parametri(demon[0],demon[1],demon[2])
        lista_punteggi.append(punteggio)
        lista_punteggi_sorted.append(punteggio)
    lista_punteggi_sorted.sort(reverse=True)

def crea_lista_finale():
    for elemento in lista_punteggi_sorted:
        lista_finale.append(lista_punteggi.index(elemento))

def crea_classifica(lista_punteggi):
    classifica = sorted(range(len(lista_punteggi)),key=lista_punteggi.__getitem__)
    classifica = classifica[::-1]
    return classifica
classifica = []
# file 1

with open('03.txt') as f:
    si,smax,t,d = [int(x) for x in next(f).split()]
    demons = []
    for line in f: # read rest of lines
        demons.append([int(x) for x in line.split()])

crea_lista_punteggi(demons)
crea_lista_finale()
classifica = crea_classifica(lista_punteggi)

with open("output03.txt","w") as txt_file:
    for elemento in classifica:
        txt_file.write(str(elemento) + "\n") 




