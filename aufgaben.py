#!/usr/bin/env python 3
"""
zahlen = [10,20,5,8,12]
for index in range (len(zahlen)):
    zahlen[index] = index * 2
print (zahlen)

zahlen = [10,20,5,8,12]
for z in zahlen:
    print(z)

zahlen = [3,7,2,9,4]
for z in zahlen:
    if z > 5:
        print(z)

i = 1

while i <= 5:
    print(i) #hier spielt die Reihenfolge in Zeile 20 und 21 eine Rolle, da Python in dieser Reihenfolge bei 5 stoppt,
    i = i +1 # da es erst printet und dann + 1 addiert. Python merkt vor dem nächsten Schleifendurchlauf somit 6> 5 und stoppt vor print.
            # andersherum würde python die Runde 5 + 1 noch mit printen, da erst in der nächsten Runde gemerkt wird das unsere Bedingung False ist.

zahlen = [2,4,6,8]

summe = 0

for z in zahlen:
    summe += z
print (summe)

zahlen = [1,3,5,7]      #Liste von zahlen
for i in range(len(zahlen)):    # hier geben wir python die Info alle indizes in der obigen Klammern zu nehmen.
    zahlen[i]*= 2 
print(zahlen)

zahlen = [1,3,5,7]             #In den folgenden 2 codes wird der Unterschied zwischen Indizes(0,1,2,3) und Werte der Indizes (1,3,5,7) klar.
for i in range(len(zahlen)):    
    zahlen[i] =zahlen[i] * 2    # Hier sagen wir python das es mit den werten der Indizes rechnen soll.
print(zahlen)

zahlen = [1,3,5,7]
for i in range(len(zahlen)):
    zahlen[i] = i *2            #Hier sagen wir Python, dass es mit den Indizes ansich rechnen soll.
print(zahlen)

zahlen = [10,10,10,10]
for i in range(len(zahlen)):
    zahlen[i] = zahlen [i] + i
print(zahlen)

zahlen = [2,4,6]
neu = []
for z in zahlen:
    neu.append(z*2)
print (neu)
print(zahlen)

zahlen = [1,5,7,8,12,24,35]
neu = []

for t in zahlen:
    neu.append(t*2)
print(neu)
print(zahlen)

zahlen = [1,3,4,8,17,23,45,65,78] #Liste der Zahlen
neu_doppel =[]                     # Neue Liste für Rechenoperation verdoppeln
neu_trippel = []                    # Neue Liste für Operation verdreifachen
for t in zahlen:                    # Schleife für Wiederholungen die ma kennt
    neu_doppel.append(t*2)          # Python für Liste doppel den Rechenbefehl geben
    neu_trippel.append(t*3)         #Python für Liste trippel den Rechenbefehl geben
print(neu_doppel)                   #Ausgaben der 3 Listen
print(neu_trippel)                  #Sobald ich eine neue Liste baue (append), brauche ich keinen Index.
print(zahlen)                       #Sobald ich eine bestehende Liste geziehlt verändern möchte, brauche ich den Index



zahlen = [3,12,5,20,7,15]
neu = []                    #hier erstellen wir eine neue Liste für bestimmte Werte die unter der for Schleife definiert und hinzugefügt werden.

for t in zahlen:            #kein index nötig, da wir eine neue Liste bauen möchten. Hier wird mit den werten gearbeitet
    if t > 10:
        neu.append(t*2)
print(neu)

zahlen = [5,5,5,5]              #Die Werte in der Klammer können als "alte" Wete beschrieben werden, da sie da sind um verändert zu werden.
for i in range(len(zahlen)): 
    zahlen[i] = zahlen[i] + i      #hier taucht der Index auf ( +i);Python weiß jetzt das es die alten werte + den index ausgeben soll
print(zahlen)

zahlen = [0,0,0,0,0]                #Die ursprünglichen Nullen sind hier nicht relevant. sie sind quasi nur Zähler der Indizies
for i in range(len(zahlen)):
    zahlen[i] = i *5                #Wir rechnen hier mit Indizes
print(zahlen)

zahlen = [2,4,6,8]
neu = []
for i in range(len(zahlen)):              #Hier möchte ich die bestehende Liste geziehlt verändern
    neu.append(zahlen[i]*i)
print(neu)

zahlen = [1,2,3,4]
neu = []
for t in zahlen:
    neu.append(t*3)
print(neu)

zahlen = [10,10,10,10]
neu = []
for i in range(len(zahlen)):
    neu.append(zahlen[i] + i)
print(neu)

zahlen = [2,7,4,9,6]
neu = []
for t in zahlen:
    if t > 5:
        neu.append(t*2)
print(neu)

zahlen = [5,5,5,5,5]
neu =[]
for i in range(len(zahlen)):
    if i % 2 == 0:
        neu.append(zahlen[i] *2)
    else:                           #hier kann ein else gesetzt werden, da es hier nicht um Zahlen geht die besispielsweise durch zahlen geteilt werden.
        neu.append(zahlen[i] *3)       #die Bedingung ist eindeutig und deshalb hier else. Wäre die Bedingung nicht eindeutig müssten wir noch ein If setzen
print(neu)                              #damit python auch weiter prüft und nicht schon beim ersten True ausgibt.NUR EIN BEDINGUNG MÖGLICH

zahlen = [1,2,3,4]
neu=[]
for i in range(len(zahlen)):
    neu.append((i+1)*zahlen[i])
print(neu)
"""
zahlen =[3,5,7]
neu = []
for t in zahlen:
    neu.append(t *2)
print(neu)

zahlen = [1,8,3,10,4]
neu = []
for t in zahlen:
    if t > 5:
        neu.append(t*2)
print(neu)

zahlen = [0,0,0,0]
neu =[]
for i in range(len(zahlen)):
    neu.append(i)
print(neu)

zahlen = [2,4,6,8]
neu = []
for i in range(len(zahlen)):
    neu.append(i * (zahlen [i]))
print(neu)

zahlen = [10,10,10,10,10]
neu =[]
for i in range(len(zahlen)):
    if i % 2==0:
        neu.append(zahlen[i]+1)
    else:
        neu.append(zahlen[i]+2)
print(neu)

zahlen=[5,10,15,20]
neu=[]
for t in zahlen:
    if t > 5 and t < 20:
        neu.append(t*2)
    elif t > 15:
        neu.append(t*4)
    else:
        neu.append(t*0)
print(neu)












