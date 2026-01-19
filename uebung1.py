#!/usr/bin/env python3
"""alter = 19
if alter < 6:
    print("Kindergarten")
elif 6>= alter <=17:
    print("Schule")
else:
    print("Erwachsen")


zahl = 13
if zahl % 2 == 0:
    print("gerade")
else:
    print ("ungerade")

n = 1
while n < 10:
    print ("n ist " , n)
    n+= 2

zahlen = [2, 4, 6, 8, 10]
for zahl  in zahlen:
    
    print ("Zahl aus der Liste mal 2:" , zahl * 2)

zahlen = [1, 2, 3,4,5,6,7,8,9]
for i in zahlen:
    print(i , " ist jetzt" , i*2)

essen = []
gericht1 = input ("Gib dein erstes Lieblingsessen ein:")
gericht2 = input ("Gib dein zweites Lieblingsessen ein:")
gericht3 = input ("Gib dein drittes Lieblingsessen ein:")


essen.append (gericht1)
essen.append (gericht2)
essen.append (gericht3)

print ("\nDeine Lieblingsessen:")
for i in range(len(essen)):
    print (i + 1, ":", essen [i])

filme = [] 

film1 = input ("Nenne deinen Lieblingsfilm:")
film2 = input ("Nenne deinen zweitliebsten Film:")
film3 = input ("Nenne deinen drittliebsten Film:")

filme.append (film1)
filme.append (film2)
filme.append (film3)

print ("\nDeine Lieblingsfilme:")
for i in range(len(filme)):
    print( i +1,  ":" , filme [i])

serien = []


serie1 = input ("Serie Nummer 1.:")
serie2 = input ("Serie Nummer 2.:")
serie3 = input ("Serie Nummer 3.:")

serien.append (serie1)
serien.append (serie2)
serien.append (serie3)

print ("\nDeine Lieblingsserien:")
for i in range(len(serien)):
    print ( i + 1, ":" , serien [i])

ld = [] # Name der Liste

La = input ("Welches Auto findest du am besten?:")  # Eingabe für die Abfrage (Kürzel reicht hier vor dem = aus um Zeit und Text zu sparen)
Lr = input ("Welches Restaurant ist das beste deiner Stadt?:")# Hinzu kommen die Fragen die unten im Terminal auftauchen.Lr = input ("Welches Restaurant ist das beste deiner Stadt?:") 
Lf = input ("Welche Farbe findest du am schönsten?:")
Ls = input ("Welches X-Box Spiel ist dein Favorite?:")
Lt = input ("Welches ist dein Lieblingstier?:")

ld.append (La) # vor dem append muss immer der Name der leeren Liste stehen. Dahinter in Klammern dann die Kürzel/Benennungen der inputs!
ld.append (Lr)
ld.append (Lf)
ld.append (Ls)
ld.append (Lt)

print("\nDeine Lieblingsdinge:")        # hier sehen wir ein neues Zeichen \n bedeutet das hier ein Enter gedrückt wird.
for i in range (len(ld)):               # i ist ein Index welcher in der range (Länge der Range hier 5 zählt, aber bei 0 startet.
    print (f"{i + 1} :  {ld [i]}")      #Darum ist es wichtig python noch zu errinern das es dochh bitt mit i + 1 startet, 
                                        #damit die Liste auch bei 1 startet. der doppelpunkt ist wiederrum ein Stringtext welcher extra ausgegeben wird.
                                        # wichtig sind auch die Kommas (nur bei simplen Sachen), und da ld [i] bedeutet das es um die angelegte Liste ld[] geht
                                        # das f steht für eine String welches auch ohne print genutzt werden kann. Bsp text = f"{i+1}: {ld[i]}. dann muss man nur
                                        #noch print (text) coden

frage = [] # Brauchen wir hier nicht,da wir die Werte direkt ausgeben und nicht speichern!

n = input ("Name:") 
a = input ("Alter")
lf = input ("Lieblingsfarbe")

frage.append (n) # Mit append speichern wir die Eingaben in einer Liste damit wir sie später gesammelt ausgeben können.
frage.append (a)
frage.append (lf)

print ("\nAusgabe:")
print(f"{n} ist {a} Jahre alt und seine Lieblingsfarbe ist {lf}")
"""

"""
n = input ("Name:")
a = int(input ("Alter:"))           # da Alter an sich ein String ist wir aber eine Zahl eingeben schreiben wir int(input ("...)) 
ls = input ("Lieblingssport:")      #damit python weiß, dass es sich bei diesem String um eineninteger handelt. (a nicht als Text sondern Zahl behandelt wird)

# auch hier speichern wir nichts, daher keine Liste nötig
if a < 18:
    print (f"Du bist noch zu jung {n}")
elif 18 <=  a <= 40:
    print (f"Beste Zeit deines Lebens {n}")
elif  a > 40:
    print (f"Erfahrung ist Gold wert {n}")
if ls == "Fußball":                             #wichtig ist das der String nur funktioniert, wenn der Text exakt gleich eingegen wird im Terminal
    print (f"Ole Ole {n} ! Fußball ist Legende")
print (f"{n} ist {a} Jahre alt ung liebt{ls}.")

"""
"""
n = input ("Name")
a = int(input ("Alter:"))
ls = input ("Lieblingssport")

print ("\nAusgabe")
print (f"{n} ist {a} Jahre alt und liebt {ls}")
"""
"""
n = input ("Name:")
a = int(input("Alter:"))
ls = input ("Lieblingssport:")

if ls == "Fußball":
    print("Ballkünsteler")
elif ls == "Boxen":
    print ("Schlagfertig")
else:
    print ("Sehr nice")
print (f"Du bist {n} und bist {a} Jahre alte und liebst {ls}.")
"""
"""
ld = []

le = input("Nenne mir bitte dein Lieblingsessen:")
lf = input("Nenne mir bitte deine Lieblingsfarbe:")
lt = input("Nenne mir bitte dein Lieblingstier:")
ls = input("Nenne mir bitte dein Lieblingsspiel:")

ld.append (le)
ld.append (lf)
ld.append (lt)
ld.append (ls)

print("\nMeine Lieblingsdinge")
for i in range (len(ld)):
    print(f"{i + 1}: {ld [i]}")
"""
n = input("Name:")
a = int(input("Alter:"))
le = input("Lieblingsessen:")

print ("\nMiniprofil")
print(f"Du bist {n}, bist {a} Jahre alt und liebst {le}")

if a >= 18:
    print("Volljährig")
else:
    print("Noch nicht volljährig")

ld = []

ls = input("Lieblingsstadt:")
le = input ("Lieblingsgeschäft:")
ll = input("Lieblingsland:")
lf = input ("Lieblingsfilm:")

ld.append (ls)
ld.append (le)
ld.append (ll)
ld.append (lf)

print("\nMeine Lieblingsdinge")
for i in range (len(ld)):
    print(f"{i + 1} : {ld [i]}")










 









