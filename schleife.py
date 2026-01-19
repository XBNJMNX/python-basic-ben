#!/usr/bin/env python 3
"""
zahlen = [1, 2, 3, 4, 5]
for zahl in zahlen:
  print ("Zahl aus der Liste:" , zahl)
for i in range (1, 6):
  print("Aktueller Wert von i:", i)
count = 0 
while count < 25:
  print(" count ist:" , count)
  count += 1
n = 10
while n > 0:
  print( "n ist:" , n)
  n-= 2
zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for z in zahlen:
  print ("Liste aus meine Zahlen:" , z)
n = 10
while n > 0:
  print ("n ist:" , n)
  n -= 1
n = 20
while n > 0:
  print("Gerade Zahlen zwischen 20 und 0:" , n)
  n -= 2
count = 1
while count < 25:
  print ("Von 1 bis 25:", count)
  count += 1

n = 10
while n > 0:
  print ("n ist " , n)
  n-=1
print("Start!")

x = 3  #Hier gebe ich den Startwert ein welcher wichtig ist, damit Python weiß das x der Startwert ist. Der Buchstabe spielt hier keine Rolle
while x < 500: #solange x < 500 ist werden die Werte ab drei immer weiter verdoppelt. Die erste Verdopplung ist 6.
  x = x*2 #hier bekommt python die Aufgabe jeden nächsten Wert zu verdoppeln.
  if x < 500: #WICHTIG! damit wir auch wirklich nur Zahlen unter 500 ausgeben, muss nach der Verdopplung noch von python geprüft werden, ob die nächste Verdopplung 500 überschreitet.
              #ansonsten würde Python die 384 noch einmal verdoppeln und den nächsten Wert ungewollt mit ausgeben.
    print( x) #WICHTIG! WHILE BEDINGUNGEN LAUFEN SOLANGE BIS EINE bEDINGUNG ERFÜLLT IST!



i = 0 #i gibt an das wir bei 0 starten.
for i in range (0, 41): #hier sagen wir python, dass es sich um eine FOR-SCHLEIFE handelt und diese wird benutzt um dinge zu beschreiben bei denen man weiß wie oft sie vorkommen.
  if i % 3 != 0:        # man kann somit eine konkrete Range definieren. Danach braucht python die Info das es nur die Werte ausgibt, welche nicht durch drei teilbar sind.
                        #Kleiner Exkurs: das i % 3 != 0: gibt Python den Befehl zu prüfen, ob Zahlen durch 3 teilbar sind. Kann man die Zahl ohne Rest durch 3 teilen kann sie durch
                        #Das i nach if ist immer die aktuelle Zahl im Durchlauf und wird hier geprüft. (Wie bei der Kleiderordnung im Club.Du kommst hier nicht rein.)
                        #Die if Zeile ist hier der Türsteher.
    print (i)

dogs= ["Krümel" , "Sugar", "Voodoo", "Coco"] # =[]  steht für Liste 
for name in (dogs):                         # Wir wissen die Namen und nutzen deshalb die for schleife für name in (dogs)

  print(name, "ist ein guter Hund") #Python checkt durch das Wort name die Liste oben ab und schreibt jetzt für alle name Den Hundenamen + den String dazu. 
                                    #es nimmt quasi in jedem Durchlauf ein Element aus der Liste und speichert es on der Variablen name.


qs = 0 # Wir geben python den Auftrag qs (Quersumme) startet bei 0
n = 485 #wir möchten das Python die quersumme aus n berechnet. 

while n > 0: #WHILE SCHLEIFE BEDEUTET WIEDER PYTHON GEHT DEN bEFEHL SOLANGE DURCH BIS WIR BEI 0 ANGEKOMMEN SIND!
  qs+= n %10 #qs+= n % 10 bedeutet das Python sich die letzte Zahl hier die 5 abschneidet, um die letzte/erste Ziffer für die Quersumme zu bekommen. 
  n //= 10   #Dann nimmt Python den wert noch durch 10 aber nimmt durch // nur einen ganzzahliges ergebnis. Dadurch kann python aus der 
print (qs)    #vorherigen 485 eine 48 machen, da 485//10 bei python 48 bedeutet. Jetzt gehts in die nächste Runde und Python liebt es Zahlen abzuzwacken:)


for n in range (0, 101): #For Schleife für vorgegebene Range
  if n % 2 == 0: #Die If Bedingung gibt Python die Aufgabe zu schauen, ob die Zahl durch 2 ohne Rest teilbar ist. Tut sie das kann Sie durch.
    print (n)

x = 5

for x in range (5, 200):
  x = x*2
  if x <=200:
    print(x) #GANZ WICHTIG!!! IMMER DARAUF ACHTEN DAS PRINT RICHTIG EINZURÜCKEN: NACH JEDER IF; WHILE FOR BEDINGUNG MUSS PRINT EINEN WEITER REIN RÜCKEN!

x = 21

while x >= 0:
  x-= 1

  print(x)

x = 0

for x in range (0, 51): 
 # x = x*2 #ich sage Python hier nimm jede zweite geraade Zahl
 # x = x +1 # hierdurch sage ich Python mache jede gerade Zahl ungerade
  #if x <=50:

    print(x*2+1)

summe = 0
i = 1

while i <=99:
  summe+=i
  i+=2
  

print (summe)

summe = 0
i =1

for i in range (1, 100, 2): #Der dritte Parameter der for Schleife ist die Schrittweite. Stopper also hier die 100 zählt nicht mit (1:Startwert 100:Stoppwert 2:Schrittweite)
  summe+= i
  
print (summe)


words = ["Python", "Java", "Algorythmus", "While", "For"]

for w in words:
  print( w, ">" , len(w), "Buchstaben") # Wir können hier den len(lenght) Befehlgeben der Python sagt ZÄHLE DIE ZEICHEN DER EINZELNEN WÖRTER!



x = 1

while x <=40:
  if x + 3 > 40: #Hier können wir python sagen wenn x + 3 > 40
    break         #DANN BREAK!!!
  x+=3
  
  print(x)


x = 0                                             # Hier wollen wir alle Werte von 0 - 200 ausgeben deren werte die Quersumme 10 haben.
                                                  # für Quersummen braucht python für alle Stellen ein Befehl. Einer, Zehne, Hunderter, Tausender usw. 
for x in range (0, 200):                          # müssen für Python erkenntlich gemacht werden. (x//1000)%10 gilt für Tausender. Das System ist bis zu den Zehnern
  if ((x// 100)%10 + (x % 10)+ (x//10)%10) == 10: #abwärtskompatibel heißt selbe Schreibweisenur mit 10 statt mit 100. für einer brauchen wir nur x%10 da wir nur eine Einerstelle überprüfen.
  
    print (x)




while input ("Passwort  ") != ("1234"):
    print("Falsches Passwort")

print ("Hereinspaziert")



for i in range ( 1, 15):
  if i % 3== 0:
    print("Fizz")
  else:
    print( i)



summe = 0
i=0

for i in range (0, 30, 2):
  summe+= i
print(summe)  


text = "Hello Python World"
#for t in text:
print( len(text))

summe = 0 #hier wird addiert!! Wie groß ist die Summe der werte?
i = 1

for i in range (1,101):
  summe+= i
print (summe)

text = "python"
print (text[0]) #hier trennt python das Wort in Zeichen 0 1 2 3 4 5 6 usw. 0 steht für das p
print (text[-1])# die - 1 sagt python von hinten an zu zählen. deshalb haben wir hier das n.
print (text[2:5]) # hier wird die Range von 2 - 5 genommen, sprich 2,3,4 ; 5 ist hier der Stopper


count = 0 # count zählt nur ereignisse oder wie oft etwas passiert

for i in range (1, 10):
  if i % 3 == 0:
    count+=1
print(count)

"""
n = int(input("Schreibe eine Zahl:")) #Alles was der User eingibt kommt als Text rein. Wir müssen Python sagen der Text ist eine Zahl die verglichen werden soll. 
if n > 10:                            #Hier nach der Größe!
  print("Groß")
else:
  print("klein")
  


  





  
 
  

