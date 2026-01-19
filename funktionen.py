# Das ist ein Kommentar in Ihrer Uebungsdatei
"""


def variablen_ausgaben (parameter): #Hier wird die Funktionn nur definiert (def), nicht aktiviert (parameter = Platzhalter)
  print("Die Funktion hat den Parameter" , parameter , "bekommen.")


def summe(parameter_a, parameter_b):
    summe = parameter_a + parameter_b
    return summe

mein_parameter = 5
variablen_ausgaben(mein_parameter) #Hier wird dir Funktion1 aufgerufen

mein_parameter_2 = 6
meine_summe = summe(mein_parameter, mein_parameter_2) #Hier wird die Summenfunktion aufgerufen die die Summe aus dem Parameter 2 retuniert
                                                    #Die reihenfolge im FUNKTIONSAUFRUF bestimmt, welcher Wert welchem parameter zugeordnet wird
variablen_ausgaben(meine_summe) #hier wird die erste Funktion wieder aufgerufen 


def differenz (parameter_a, parameter_b):
    return parameter_a - parameter_b


mein_parameter = 10
mein_parameter_2 = 3

meine_differenz1 = differenz(mein_parameter, mein_parameter_2)
meine_differenz2 = differenz(mein_parameter_2, mein_parameter)
print(meine_differenz1)
print(meine_differenz2)


def quadratzahl (a):
    return a**2

a = 5

meine_quadratzahl = quadratzahl(a)
print(meine_quadratzahl)

def doppel (a):
    return a * 2

a = 4

mein_doppel = doppel(a)
print(mein_doppel)

def groeßer_kleiner (a, b):
    if a > b:
        return True
    else:
        return False
a = 2
b = 7

mein_groeßer_kleiner = groeßer_kleiner(a ,b)
print(mein_groeßer_kleiner)

def zahlen_liste (liste):
    summe = 0
    for zahl in liste:
        summe += zahl
    return summe #Hier ist es wieder wichtig das return aus der Schleife (Ergenis alle Durchläufe) zu nehmen da Sie sonst bei der 1 schon stoppt.
zahlen = [1,2,3,4,5,6,7,8,9,10] #return heißt jetzt ist Feierabend. Klappe zu Affe tot. Das heißt Return in der schleife nach der ersten Runde pleite.:))(sofortiger Abbruch)
ergebnis = zahlen_liste(zahlen)
print(ergebnis)

def ausgabe_meine_liste (liste):
    print("Das ist die erstellte Liste:" , liste) #bei dieser Funktion wird nur die Liste wieder ausgegeben,
                                                # da wir nicht mit einer for Schleife jedes Element einzeln nutzen
liste = [1,3,5,7,9]
ausgabe_meine_liste(liste)

def ausgabe_meine_liste (liste):
    for element in liste:                   #hier werden die Elemente der Liste einzeln ausgegeben durch die for schleife
        print("Element:" , element)
test_liste = [1,2,3,4,5,6,7,8,]
ausgabe_meine_liste(test_liste)

def rechnung (a,b):
    ergebnis = (a * (b +2))
    return ergebnis
test_a = 3
test_b = 4

test_ergebnis = rechnung(test_a, test_b)
print(test_ergebnis)

def rechnung (a,b):         
    return (a *(b+2))
a = 4
b = 5

testergebnis = rechnung(a, b)
print("Das Ergebnis" , testergebnis)

def kleiner_als (a,b,c):
    if a < b and b < c:
        return True
    else:
        return False
a = 2
b = 2
c = 3

mein_kleiner_als = kleiner_als (a,b,c)
print(mein_kleiner_als)

def rechnung (a,b,c,d,e,f): #Name der funktion + parameter
    return (a+(b*c)-(d**2)+(e/f)) #returnierung der Funktion nach berechnung/Die Berechnung wird erst im unteren Teil befohlen
a=2
b=3
c=5
d=1     #Parameter definition
e=4
f=2

ergebnis = rechnung(a,b,c,d,e,f)    #ergebnis oder irgendein Wort oder buchstabe = name der funktion(parameter)
print("Das Ergenis ist", ergebnis)      #print immer das Wort oder den Buchstaben der dem Funktionsnamen zugewiesen ist

def ist_es_richtig (a,b,c,d,e):
    if a < b < c < d < e:
        return True
    else:
        return False
a = 1
b = 0
c = 3
d = 4
e = 5

ergebnis = ist_es_richtig(a,b,c,d,e)
print("Das Ergenis ist", ergebnis)
"""
import math
def quadratic_formula (a,b,c):
    D = b**2 - 4*a*c
    if D < 0:
        print("Leider gibt es keine Lösung bro")
        return False
    elif D == 0:
        print("Es gibt genau eine Doppellösung, und zwar:")
        return x, x 
    else:
        print("Hier gibt es zwei Lösungen welche lauten:")
    wurzel = math.sqrt(D)
    x1 = (-b + wurzel) /(2*a)
    x2 = (-b - wurzel) /(2*a)  
    x = (-b + wurzel) /(2*a) == (-b)/(2*a)
    x = (-b - wurzel) /(2*a) == (-b)/(2*a)
    return x1, x2

a = float(input("Gib bitte a ein"))
b = float(input("Gib bitte b ein"))
c = float(input("Gib bitte c ein"))


x1, x2 = quadratic_formula(a,b,c)
x, x = quadratic_formula(a,b,c)
print("x1 =", x1)
print("x2 =", x2)
print("Doppellösung =",x, x)