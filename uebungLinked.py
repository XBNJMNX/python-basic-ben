#!/usr/bin/env Python 3
"""
a = 3 
b = 10

while(a <= b):
  a = a + 3
  b = b + 1

print("a ist das erste mal größer als b")
print("a" , a)
print("b" , b)

zahlen = [12, 34, 56, 76, 99, 32, 1, 5, 72, 6]
anzahl = 0 #Hier geht es darum eine bestimmte Anzahl zu ermitteln; nicht die Werte selbst
for x in zahlen: # hier bekommt python die Info die Zahlen der liste durchzugehen. Dafür brauchen wir eine Variablen namens hier x
  if x >= 50:   #desweiteren sagen wir python, dass es für ale Werte die >= 50 sind
    anzahl = anzahl + 1 # die Anzahl der werte ab wert 0 hinzuaddiert
print("Anzahl der Zahlen >= 50" , anzahl) #hier möchten wir die Anzahl der Zahlen >= 50 bekommen nicht die Zahlen selbst

zahlen = [10, 25, 30, 5, 45, 12,22,50]
anzahl = 0
for x in zahlen:
  if x > 20:
    anzahl += 1
print("Anzahl der Zahlen größer als 20:" , anzahl)

zahlen =[2, 12, 45, 6, 98, 105, 23, 17, 3, 1]
anzahl = 0
for x in zahlen:
  if x <= 10:
    anzahl += 1
print("Anzahl Zahlen <= 10:", anzahl)


a = 5
b = 20

while a <= b:
  a = a + 3
  b = b + 1
print("a ist das erste Mal größer als b")
print("a" , a)
print("b" , b)



a = 4
b = 12
c = 24

while True:

  a = a + 7
  b = b + 4
  c = c + 2

  if a > b and a > c:

    print("a überholt b und c zum ersten Mal:")
    print("a" , a)
    print("b" , b)
    print("c" , c)

    break
  
a = 4
b = 12
c = 24

while a <= b or a <= c: #Hier MÜSSEN wir ein or setzen, denn unsere while Schleife läuft nur solange unser Ereignis True ist.
  a_alt = a             #d.h. sobald a einen von den beiden anderen überschreitet hört die schleife auf da wir ein False True Ereignis haben.
  b_alt = b             #bei or ist False True aber immer noch True und die Schleife läuft so lange weiter bis wir False False haben. Dann Stop!
  c_alt = c

  a = a + 7
  b = b + 4
  c = c + 2
print("Letzer Zustand vor dem Überholen")
print(a_alt, b_alt, c_alt)
print("Zustand nach dem Überholen:")
print(a, b, c)


        # 0,1,2,3,4,5,6,7; Das sind die Indizes der Zahlen darunter               
zahlen = [0,0,0,0,0,0,0,0]
for index in range (len(zahlen)): #Hier hilft uns dasd (len(zahlen)) lenght=länge die Zahlenanzahl der Liste zu ermitteln
  zahlen[index] = (index) *3      # wichtig ist das wir python sagen es soll die Indizes und nicht die Zahlen selbst mit drei Multiplizieren
print(zahlen)                     


zahlen = [0,0,0,0,0,0,0,0,0]
for index in range (len(zahlen)): #index meint Indizes(Mehrzahl von Index)
  zahlen[index] = index *3
print(zahlen)


zahlen = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for index in range (len(zahlen)):
  zahlen[index] = index *3
print (zahlen)


zahlen = [3,44,1,7,22,91,55,4,100,13]   
anzahl = 0                            #Hier möchten wir eine bestimmteAnzahl an Zahlen aus der Liste ermitteln.
for x in zahlen:                      #Das x steht hier als Variable und Python fügz für x jede Zahl nacheinander ein,
  if x >= 20:                         #um zu prüfen, ob diese Zahl das Kriterium >= 20 erfüllt.
    anzahl += 1                       # Hier werden die Zahlen die Größer sind gespeichert und aufaddiert.
print("Anzahl der Zahlen größer gleich 20:" , anzahl)

zahlen = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for index in range (len(zahlen)):
  zahlen[index] = index*3
print(zahlen)

zahlen = [3,44,1,7,22,91,55,4,100,13]
for x in zahlen:
  if x % 11 == 0: #hier geht es darum das Python herausfindet, welche Zahlen aus der Liste ohne Rest durch 11 teilbar sind.

    print(x)

zahlen = [12,13,14,15,16,17,18]
for x in zahlen:
  if x % 2 == 0:
    print(x)


werte = [10,20,5,8,12]
for index in range(len(werte)):
  werte[index] = index + index #Hier bekommt Python den Befehl die indexe mit ihrem eigenen Wert zu addieren
print(werte)                    #d.h. 0+0; 1+1; 2+2 usw.


werte = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
for index in range (len(werte)):
  werte[index] = index + index
print (werte)


a = 5
b = 20
c = 40

while a <= b or a <= c:
  a_alt=a
  b_alt=b
  c_alt=c

  a= a + 6
  b= b + 3
  c= c + 1
print("Letzter Zustand von a vor dem Überholen gegenüber b und c")
print(a_alt, b_alt, c_alt)
print("Erster Zustand von a nach dem Überholen gegenüber b und c")
print(a,b,c)

a = 17
b = 2
c = -4

while c <= b or c <= a:
  a_alt=a
  b_alt=b
  c_alt=c

  a = a + 1
  b = b + 4
  c = c + 6

print("Letzter Zustand von c vor dem Überholen")
print(a_alt,b_alt,c_alt)
print("Erster Zustand von c nach dem Überholen")
print(a,b,c)


a = 2
b = 15
c = 40
d = 60

while a<=b or a<=c or a<=d: #wichtig! ist hier wieder das or da wir es hier benötigen damit Python nicht schon stoppt wenn eins
                            #False ist.
  a_alt= a                  #Hier bekommt python den Befehl die den aktuellen Wert von der variablen zu sichern bevor es ihn ändert.
  b_alt=b
  c_alt=c
  d_alt=d

  print("Vor Update:" , a_alt,b_alt,c_alt,d_alt) #Hier gibt python durch das print jeden Zwischenschritt vor der Veränderung aus! 
  #zeig mir später/speicher die Zahlen jetzt sofort!!! Jede Runde wird gespeichert un später ausgegeben.
  a += 10
  b += 4
  c += 3
  d += 1

  print("Nach Update" , a,b,c,d) #Hierdurch gibt Python jeden Schritt nach der Veränderung aus.

print("Letzter Zusatnd von a vor dem überholen") #Die letzten beiden Runden sind für unsere Schleife extra zu betrachten und wichtig!!!
print(a_alt,b_alt,c_alt,d_alt)
print("Erster Zusatnd von a nach dem Überholen")
print(a,b,c,d)

# in dieser Aufgabe hatte ich keine Listen angelegt
zahlen = [2,15,33,48,99,123,8,6,51]
for zahl in zahlen:
  if zahl < 20:
    print("Zahlen in der kleinen Liste=" ,zahl)
  elif zahl >= 50:
    print("Zahlen in der großen Liste=" ,zahl)
# was dazu führte, dass die Zahlen im Terminal richtig angezeigt wurden, jedoch nicht in Listen.




zahlen = [2,15,33,48,99,123,8,6,51]

klein = []
groß = []

for zahl in zahlen:
  if zahl < 20:
    klein.append(zahl)
  elif zahl>= 50:
    groß.append(zahl)
print("Kleine Liste", klein)
print("Große Liste" , groß)


zahlen = [3,12,25,41,50,7,99,18,67,4,29,85]

klein = []
mittel = []
groß = []

for zahl in zahlen:
  if zahl < 20:
    klein.append(zahl)
  elif 20<= zahl <= 49:
    mittel.append(zahl)
  elif zahl >= 50:
    groß.append(zahl)
print("KLeine Liste", klein)
print("Mittlere Liste", mittel)
print("Große Liste", groß)

"""
zahlen = [5,10,12,15,21,25,30,33,40,44,50]

durch_5=[]
durch_3=[]
durch_keins=[]

for zahl in zahlen:
  if zahl % 5 == 0:
    durch_5.append(zahl)
  if zahl % 3 == 0:   #hier nehmen wir 3*if damit wenn zahlen zufällig durch 5 und 3 teilbar sind, dass sie trotzdem in beiden Listen erwähnt werden.
    durch_3.append(zahl) #würde man elif machen dann würde die 15 und die 30 einfach nur bei der Liste durch 5 teilbar erscheinen da dort das ereignis schon True wäre
  if zahl % 3 and zahl % 5 != 0:  #und Python dann gar nicht weiter prüft. #MEHRERE BEDINGUNGEN MÖGLICH
    durch_keins.append(zahl)
print("Durch 5 teilbar" , durch_5)
print("Durch 3 teilbar" , durch_3)
print("Durch keins teilbar" , durch_keins)

"""

werte = [4,9,13,22,5,31,42,7,18,90]

gerade_indizes= []
ungerade_indizes= []
über_20=[]

for index in range (len(werte)):
  if index % 2 == 0:
    gerade_indizes.append(index)
  if index % 2 != 0:
    ungerade_indizes.append(index)
for wert in werte:
  if wert > 20:
    über_20.append(wert)
print("Gerade Indizes" , gerade_indizes)
print("Ungerade Indizes" , ungerade_indizes)
print("Über 20" , über_20)

liste_a = [3,12,55,22,1,80,14]
liste_b = [10,5,60,21,3,19,99]

summe_liste = []
max_liste = []
gleich_liste = []

for index in range (len(liste_a)):
  a_wert = liste_a[index]
  b_wert = liste_b [index]

  summe_liste.append(a_wert + b_wert)

  if a_wert > b_wert:
    max_liste.append(a_wert)
  else:
    max_liste.append(b_wert)
  
  if a_wert == b_wert:
    gleich_liste.append(a_wert)
print("Summe aus a und b" , summe_liste)
print("Größerer von a und b" , max_liste)
print("Beide gleich" , gleich_liste)
"""

    




