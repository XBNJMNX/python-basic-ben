#!/usr/bin/env python3
def spielfeld(feld_liste):
    for i in range(0, 9, 3): #Startwerte 0,3,6
        if 0 < i <= 6: #wenn das eintrifft print Linie nach null und nach 3
            print("---------") 
        print(feld_liste[i],"|", feld_liste[i+1],"|", feld_liste[i+2]) #jede Reihe bekommt 2 neue Werte
feld_liste= [1,2,3,4,5,6,7,8,9] #Werte in der Feldliste(Indizes laufen im hintergrund) Python brauch die Info um später die 
                                #Eingaben von 1-9 zuordnen zu können.
#spielfeld(feld_liste) brauchen wir hier nicht da es später noch kommt

def gewinn_abfrage(feld_liste, spieler): #parameter sind wichtig für die Zuordnung in der Funktion
    #Zeilen Abfrage
    if feld_liste[0] == feld_liste[1] == feld_liste [2] == spieler: #feld_liste und Spieler gewinn
        return True
    if feld_liste[3] == feld_liste[4] == feld_liste [5] == spieler:
        return True
    if feld_liste[6] == feld_liste[7] == feld_liste [8] == spieler:
        return True
    #Spaltenabfrage
    if feld_liste[0] == feld_liste[3] == feld_liste [6] == spieler:
        return True
    if feld_liste[1] == feld_liste[4] == feld_liste [7] == spieler:
        return True
    if feld_liste[2] == feld_liste[5] == feld_liste [8] == spieler:
        return True
    #Diagonale
    if feld_liste[0] == feld_liste[4] == feld_liste [8] == spieler:
        return True
    if feld_liste[6] == feld_liste[4] == feld_liste [2] == spieler:
        return True
    return False

def abfrage_unentschieden (feld_liste): 
    unentschieden = True #unentschieden erstmal für wahr erklären
    for feld in feld_liste: #Schleife die die feldliste prüft
        if feld == " ": #wenn ein feld noch leer
            unentschieden = False #kein unentschieden
    return unentschieden #alle felder voll: unentschieden

def hole_zug(feld_liste, spieler_symbol): #Funktion Eingabe der Spieler mit Fehleingabenhinweis
    while True:
        eingabe = input(f"{spieler_symbol}: wähle ein Feld von 1-9: ")
        if not eingabe.isdigit():
            print("Bitte Zahl eingeben")
            continue
        pos = int(eingabe)
        if pos < 1 or pos > 9:
            print("Bitte nur Zahlen zwischen 1 und 9 eingeben")
            continue
        index = pos -1 #Umrechnung von Nutzereingabe (1-9) zu Index (0_8)
        if feld_liste[index] != " ":
            print("Feld ist schon belegt! Wähle ein anderes!")
            continue
        return index

feld_liste = [" "]*9 #wichtig die Feldliste nochmals komplett leer angeben. Diese liste bezieht sich auf alle Funtionen ausser die Erste,
                    #welche ihre eigene Feldliste mit Werten hat.

while True:    #Hauptschleife: X und O ziehen abwechselnd,bis Sieg oder Unentschieden erreicht ist         
    spielfeld(feld_liste)
    #input_x = ("X: wähle ein Feld von 1-9: ")
    #feld_liste[int(input(input_x))-1] = "X"

    index = hole_zug(feld_liste, "X") Funktion hole_zug ausführen
    feld_liste[index] = "X"

    if gewinn_abfrage (feld_liste, "X"):
        print("Sieg Spieler X")
        break
    unentschieden = abfrage_unentschieden(feld_liste)
    if unentschieden:
        print("Unentschieden")
        break
    spielfeld(feld_liste)

    #input_o = ("O: wähle ein Feld von 1-9: ")
    #feld_liste[int(input(input_o))-1] = "O"

    index = hole_zug(feld_liste, "O")
    feld_liste[index] = "O"

    if gewinn_abfrage (feld_liste, "O"):
        print("Sieg Spieler O")
        break
    unentschieden = abfrage_unentschieden(feld_liste)
    if unentschieden:
        print("Unentschieden")
        break

    
    
    