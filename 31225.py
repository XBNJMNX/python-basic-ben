#!/usr/bin/env python 3
"""
for i in range( 1,101):
    if i % 3 == 0 and i % 5 ==0 and i % 2 != 0:

        print (i)



def qs_gerade (x): #hier wird die Funktion ersteinmal definiert. Ich könnter die Funktion auch Klaus August nennen,
    qs = 0          #müsste das dann aber unten im print auch so nennen, damit python weiß..ok es geht um die Funktion.
    while x > 0:     # die while schleife ist hier der Gamechanger, da es reicht einfach > 0 zu schreiben und ich kann unten jede x-beliebige natürliche  Zahl eingeben.
        qs += x % 10 #das wir oben qs = 0 definiert haben muss hier wieder das qs kommen. Hätten wir es kl genannt müsste hier auch kl += 0 stehen.
        x //= 10       #ganz nach dem Motto gib dem Hund einen Namen und lass ihn laufen. Für die Übersicht eignet sich qs aber sehr gut da ers ja um quersummengeht.
    if qs % 2 == 0:    #das % 10 gibt Python vor die letzte Zahl der eingegebenen Zahl abzuzwacken und als Summanden für die Quersumme zu speichern. Das //= 10 gibt dann noch die Zahl durch 10 als 
        return True     #ganzzahligen quotienten aus. Das läuft dann solange bis python bei 0 angekommen ist. Dananch wir in der if bedingung noch geprüft, ob die Quersumme durch 2 ohne Rest teilbar ist.
    else:               #return True und return False ist ebenfalls sehr wichtig damit python weiß wie es auf eingegebene Zahlen reagieren soll.
        return False
zahl = int(input("Gib bitte eineZahl ein:")) #hiermit starten wir die Funktion, indem wir ihr sagen, das es beim input um eine Zahl geht welche zum rechnen ist.
print(qs_gerade(zahl))                          #beim print sagen wir python den Funktionsnamen und den zuvor definieretn Begriff zahl. Jetzt kann python das für alle Zahlen berechen.


zahlen = [17, 22, 30, 49, 53, 61, 84, 91, 109] #Liste unserer Zahlen
def qs (x):     #Hier wird ein Rezept angelegt: qs von x.
    summe = 0   #Wir starten bei 0.
    temp = x     #hier geben wir x einen Namen. Wir könnten die Zeile aber weglassen und x = x lassen
    while temp > 0: #solange wir > 0 sind startet die Funktion wieder von vorne.
        summe += temp % 10 #hier kommen die Summanden der quersumme zusammen (Die jeweils letzute Ziffe wird hier gesaved)
        temp //=10 #dann wird die letzte Zahl abgeschnitten. Quasi durch die ganzzahligen Quotienten Rechnung Bsp: 348 // 10 = 34
                        #die 8 wird schon vorher abgegriffen aber sie ist solange noch vorhanden bis nach diesem Schritt.
    return summe    #hier soll python zur Summe kommen
ergebnis = [] #hier wird python an die obige Liste errinert


for zahl in zahlen: # jetzt bekommt python die Info das es sich hier nur um die Zahlen einer bestimmten Liste (s.o.) handelt
    if qs(zahl)  == 10: #wenn von einer der Zahlen aus der Liste die quersumme 10 ist
        ergebnis.append(zahl) #soll python diese Zahlen speichern und der Ausgabeliste hinzufügen.
print (ergebnis) #jetzt weiß python das es die gewünschten Zahlen in eine Ausgabeliste printen soll.


def add(a, b):
    result = a + b
    return result
print (add(5 , 3))
"""


