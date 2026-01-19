#!/usr/bin/env python 3
"""
zahlen = [1,2,3,4,5]
for t in zahlen:
    t *= 2
    print(t) #hier muss das print eingerückt seinda sonst nur die letzte Zahl verdoppelt wird.

zahlen = [1,2,3,4,5]
for i in range (len(zahlen)):
    zahlen[i] += 2 #zahlen aus i bedeutet überschreibe die Werte aus zahlen (jede zahl +2)
print(zahlen)

zahlen = [1,2,3,4,5]
quadrate = []
for i in range (len(zahlen)):
    quadrate.append(zahlen[i]**2)
print(quadrate)

zahlen = [3,7,10,12,15,18]
for t in zahlen:
    if t % 2 == 0:
        print(t)

zahlen = [10,20,30,40]
i = 0                   #i=0 bedeutet, dass die while-schleifde bei index 0 (hier 10) startet
while i < len(zahlen):  # while i < len... bedeutet gehe alle Indexe in der Liste nacheinander durch.
    print(zahlen[i])        #gebe alle zahlen nacheinander aus 
    i += 1                  # gehe nach jeder runde zum nächsten index-wert

zahlen = [2,4,6,8,10]
for x in zahlen:
    x = x//2
    print(x)

zahlen = [1,2,3,4,5]
for i in range(len(zahlen)):
    zahlen[i] += 1
print(zahlen)

zahlen = [5,10,15,20]
i=0
while zahlen[i] > 10: #hier ist ein Fehler wenn die Schleife bei i=0 startet und > 10 sein soll kommt aber die 5
    print(zahlen[i])        #das ist False und die Schleife endet
    i += 1
"""
zahlen = [5,10,15,20]
i=0
while i < len(zahlen): #Ebene 0 Start der While schleife
    if zahlen[i] > 10:  #Ebene 1 einmal eingerückt. Bedingung gehört zur while schleife und wir in jeder"Runde geprüft
        print(zahlen[i]) #Ebene 2 print gehört auch zur while schleife und wird ausgefürt sobald True eintrift(in dem Fall ab 15)
    i+=1 #zurück zur Ebene 1 denn alles unter 1 gehört zu while, alle unter 2 zu if => i wird immer + 1 erhöht egal ob True oder False
        #wäre i+= 1 unter if würde nur + 1 gerechnet werden wenn True, also in dem Fall gar nicht 







