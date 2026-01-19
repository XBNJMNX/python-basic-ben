#!/usr/bin/env python3
"""
def ist_postitiv (x):
    if x > 0:
        return True
    else:
        return False
x = -1
ergebnis=ist_postitiv(x)
print("Das Ergebnis ist" , ergebnis)

def summe_liste (liste):
    summe = 0
    for zahl in liste:
        summe += zahl
    return summe
test_liste = [1,2,3,4,5]
ergebnis = summe_liste(test_liste)
print("Summe der Liste =", ergebnis)

def summe_liste(liste):
    summe = 0
    for zahl in liste:
        summe += zahl
    return summe
zahlen = [1,3,2,5,4,7,8,90,67,5,3]
ergebnis = summe_liste(zahlen)
print(ergebnis)


def anzahl_elemente(liste):
    i = 1
    for i in range(len(zahlen)):
        i += 1
    return i
zahlen = [1,2,0,0,0,0,0,0,0,0]
ergebnis = anzahl_elemente(zahlen)
print(ergebnis)

def summe_gerade(liste):
    summe = 0
    for zahl in liste:
        if zahl % 2 == 0:
            summe += zahl
    return summe
zahlen = [1,2,3,4,5,6]
ergebnis = summe_gerade(zahlen)
print(ergebnis)

def summe_ungerade(liste):
    summe = 0
    for zahl in liste:
        if zahl % 2 != 0:
            summe += zahl
    return summe
zahlen = [1,2,3,4,5,6,7,8,9]
ergebnis = summe_ungerade(zahlen)
print(ergebnis)

def groesstes_element(liste):
    groesstes = liste[0] #Startzahl als kleinste definieren
    for zahl in liste:  #alle zahlen in liste einzeln durchgehen
        if zahl > groesstes: #wenn Zahl > als vorherige 
            groesstes = zahl   #merken sonst ignorieren; Schleife geht zur nächsten Zahl und prüft sie
    return groesstes            #bis alle Zahlen der Liste geprüft wurden. Ist die Größte wird retuniert. Fertig
zahlen = [1,3,5,7,9,10]
ergebnis = groesstes_element(zahlen)
print(ergebnis)

def kleinstes_element(liste):
    kleinstes = liste[0] #Startzahl als kleinste definieren
    for zahl in liste:      #alle zahlen in liste einzeln durchgehen
        if zahl < kleinstes: #wenn Zahl < als vorherige 
            kleinstes = zahl    #merken sonst ignorieren; Schleife geht zur nächsten Zahl und prüft sie
    return kleinstes               #bis alle Zahlen der Liste geprüft wurden. Ist die kleinste wird retuniert. Fertig
zahlen = [100,123,45,654,23,89,2,3,1,0]
ergebnis = kleinstes_element(zahlen)
print(ergebnis)


def summe_liste(liste):
    summe = 0
    for zahl in liste:
        summe += zahl
    return summe
zahlen = [2,3,4,5,6,7,8]
result = summe_liste(zahlen)
print(result)

def summe_vielfache_3(liste):
    summe = 0
    for zahl in liste:
        if zahl % 3 == 0:
            summe += zahl
    return summe
zahlen = [1,2,3,4,5,6,7,8,9,12,13,15,18]
result = summe_vielfache_3(zahlen)
print(result)

def anzahl_positiv(liste):
    count = 0
    for zahl in liste:
        if zahl > 0:
            count += 1
    return count
zahlen = [-4,-2,-1,-6,9,7,6,-7,0,10,12,17]
result = anzahl_positiv(zahlen)
print(result)

def content_negativ(liste):
    negativ = liste[0]
    for zahl in liste:
        if zahl < negativ:
            negativ = zahl
        return True
    else:
        return False
zahlen = [1,2,3,4,5,2,-3,-5,9,0]
result = content_negativ(zahlen)
print(result)

def groesste_gerade(liste):
    biggest_gerade = liste[0]
    for zahl in liste:
        if zahl % 2 == 0:
            biggest_gerade = zahl
    return biggest_gerade
   
zahlen = [1,2,4,5,6,8,50,98,3,12,100,124,268]
result = groesste_gerade(zahlen)
print(result)



def durchschnitt(liste):
    i = 1
    summe = 0
    anzahl = 0
    for zahl in liste:
        summe += zahl
        anzahl += i 
    return summe/anzahl
zahlen = [1,2,3,4]
result = durchschnitt(zahlen)
print(result)

def anzahl_positiv(liste):
    anzahl = 0
    for zahl in liste:
        if zahl > 0:
            anzahl += 1
    return anzahl
zahlen = [1,-2,3,-4,5,6]
result = anzahl_positiv(zahlen)
print(result)

def groesste_gerade(liste):
    groesste = liste [0]
    for zahl in liste:
        if zahl > groesste and zahl %2 == 0:
            groesste = zahl
    return groesste
zahlen = [1,2,3,4,5,6,78]
result = groesste_gerade(zahlen)
print(result)

def nur_groesser_als_5(liste):
    neue_liste=[]
    for zahl in liste:
        if zahl > 5:
            neue_liste.append(zahl)
    return neue_liste   
zahlen = [1,2,3,4,5,6,7,8]
result = nur_groesser_als_5(zahlen)
print(result)

def ist_sortiert(liste):
    i = 0
    for i in range (len(zahlen) -1):
    #liste[i]<=liste[i+1]
        if liste[i] > liste[i+1]:
            return False
    return True
zahlen = [1,2,3,4,5,3]
result = ist_sortiert(zahlen)
print(result)

def groesstes_element(liste):
    groesstes = liste[0]
    for zahl in liste:
        groesstes = zahl
    return groesstes
zahlen = [1,2,5,4,87,65,980]
result = groesstes_element(zahlen)
print(result)

def kleinstes_element(liste):
    kleinstes = liste[0]
    for zahl in liste:
        kleinstes = zahl
    return kleinstes
zahlen = [-3,-5,3,4,56,-12]
result = kleinstes_element(zahlen)
print(result)

def zahlen_groesser_5(liste):
    zahlen_groesser_5=[]
    
    count = 0
    for zahl in zahlen:
        if zahl > 5:
            count += 1
            zahlen_groesser_5.append(count)
    return zahlen_groesser_5
zahlen = [1,4,3,6,7,12]
result = zahlen_groesser_5(zahlen)
print(result)

def gerade_zahlen(liste):
    neue_liste = []
    for zahl in liste:
        if zahl  % 2 ==0:
            neue_liste.append(zahl)
    return neue_liste
zahlen = [1,2,3,4,5,6,7,8]
result = gerade_zahlen(zahlen)
print(result)

def durchschnitt(liste):
    neue_liste = []
    i = 1
    summe = 0
    anzahl = 0
    for zahl in liste:
        summe += zahl
        anzahl += i
    neue_liste.append(zahl)
    
    return summe/anzahl
zahlen = [1,2,3,4,5,6,7,8]
result = durchschnitt(zahlen)
print(result)

def streng_aufsteigend(liste):
    for i in range(len(zahlen)-1):
        if liste [i] >= liste [i+1]:#ist der erste wert >= dem nächsten return False. da wir eine streng aufsteigende Liste möchten
            return False
    return True
zahlen = [1,2,3,4,5,6,7,8,9]
result = streng_aufsteigend(zahlen)
print(result)


def liste_summe(liste):
    summe = 0
    for zahl in liste:
        summe += zahl
    return summe
zahlen = [2,4,3,5,7]
result = liste_summe(zahlen)
print(result)

def anzahl(liste):
    i = 1
    count = 0
    for zahl in liste:
        count += i
    return count
zahlen = [1,2,3,4,5,6,7,8,9]
result = anzahl(zahlen)
print(result)

def groesstes_element(liste):
    groesstes = liste[0] #wir definieren als groessten wert den ersten der Liste, weil python immer startwert braucht
    for zahl in liste:
        if zahl > groesstes: # wenn zahl > groesstes
            groesstes = zahl #wird die nächste zahl als größte definiert, falls nicht bleibt die letze groesste zahl erhalten
    return groesstes           #bis deie nächst groessere gefunden wird. nicht größere ignoriert die Schleife.     
zahlen =[1,2,4,3,5,4,7,6,89]    #Das return aus der schleife raus damit python auch alle zahlen durchgeht
result = groesstes_element(zahlen)
print(result)

def kleinstes_element(liste):
    kleinstes = liste[0]
    for zahl in liste:
        if zahl < kleinstes:
            kleinstes = zahl
    return kleinstes
zahlen = [3,4,5,2,8,7.-1,-7,-12,-1]
result = kleinstes_element(zahlen)
print(result)

def gerade_zahlen(liste):
    neue_liste = []
    for zahl in liste:
        if zahl % 2 == 0:
            neue_liste.append(zahl)
    return neue_liste
zahlen = [1,2,3,4,5,67,8,34,78,100]
result = gerade_zahlen(zahlen)
print(result)

def nur_groesser_als_5(liste):
    neue_liste = []
    for zahl in zahlen:
        if zahl % 5 == 0:
            neue_liste.append(zahl)
    return neue_liste
zahlen = (12,5,34,35,65,1,78,100)
result = nur_groesser_als_5(zahlen)
print(result)

def durchschnitt(liste):
    i = 1
    summe = 0
    anzahl = 0
    for zahl in liste:
        summe += zahl
        anzahl += i
    return summe/anzahl
zahlen = [1,2,3,4,5,6,7,8,9]
result = durchschnitt(zahlen)
print(result)

def liste_zahl(liste):
    a = 1
    for zahl in liste:
        if zahl == a:
            return True
    return False
zahlen = (2,3,4)
result = liste_zahl(zahlen)
print(result)

def streng_aufsteigend(liste):
    for i in range (len(zahlen)-1): # wir müssen Python sagen, das es beim letzten wert stoppen soll
        if liste [i] >= liste [i+1]:# ohne die -1 würde python out of range kommen da es die 12 auch checken will.
                                    #wie vergleichen immer element i mit element i +1, 
            return False            #deswegen dürfen wir nur bis zum vorletzen wert laufen der dann 11 mit 12 vergleicht
    
    return True
zahlen =[1,2,3,4,5,6,7,8,9,10,11,12]
result = streng_aufsteigend(zahlen)
print(result)

def max_gerade(liste):
    groesste_gerade = None
    for zahl in liste:
        if zahl % 2 == 0:
            if groesste_gerade is None or zahl > groesste_gerade:
                groesste_gerade = zahl
    return groesste_gerade
            
zahlen = (1,2,3,4,5,6,7,8)
result = max_gerade(zahlen)
print(result)       




x = 0
for x in range (0, 21, 2):
    if x %2 == 0:
        print(x)

summe = 0
x = 1
while x <= 100:
    summe += x
    x += 1
print(summe)


x = 1
while x <= 5:
    print(x)
    x += 1 # die x += 1 rettet uns vor der Endlosschleife, ohne die Zeile würde Python einfach endlos einsen printen
            # und nach dem print ist wichtig damit python die 6 nicht mit printet und vorher checkt das die 6 kommt.
summe = 0
x = 1
while x <= 5:
    summe += x
    x +=1
    print(summe) # in der Schleife printet python alls Zwischensummen
#außerhalb wird nur das endergebnis geprintet

x = 10
while x >= 1:
    print(x)
    x-=1

x = 1
while x <=10:
    print(x)
    x +=1

x = 10
while x >=1:
    print(x)
    x-= 1
"""    
x = 0
while 0<= x <=20: 
    print(x)
    x+=2
   
    
    






        

        
        



    
        
