#!/usr/bbin/env python 3
"""
summe = 3
i = 9
while i <=117 :
    summe+= i
    i+= 18
    print ( summe)
  
n = int(input ("Bitte gib eine Zahl ein:"))

summe = 1
i = 2
while i < n:
    i+=4
    summe += i
print ("Summe der geraden Zahlen von 0 bis", n, "ist",summe )   

"""
"""
n = int(input("Bitte gib eine Zahl ein:")) # Hier sagen wir Python nur das n die vom user eingegebene Zahlist. int istwichtig zu rechnen da ohne int ein String entsteht.

summe = 0 #Wir starten bei 0.
i = 0 #Unser Startwert beginnt ab 0, kann aber auch anderweitig, je nach vorhaben variiert werden.

while i <= n: # das while ist unser Herzstück welches Python befielt alle gerade Zahlen <= n zu addieren bis n erreicht ist.

    summe += i # Die Info braucht python zuerst damit es weiß das wir bei Null starten.
    i += 2 # dieser Wert gibt an in welchen Schritten aufsummiert wird
print("Die Summe alle gerade Zahlen <= deiner Zahl ist:")

# summe += i muss hier vor dem i += 2 stehen damit wir nicht eine zwei zu viel addieren
#python geht von oben nach untern und ist die Zeile i+=2 vor der Zeile summe+= i rechnet python noch eine Runde weiter. 
#Runde 1. wäre dann i+= 2 folgt 0 + 2 = 2 summe+= 2; zweite Runde wäre dann i+=2 2 + 2 = 4 (summe += 4) jetzt wären wir eigentlich am Ende
#aber wenn wir erst erhöhen und dann addieren denkt python es kann jetzt nochmal eine Runde drehen welche dann lautet i+= 2 2+4 summe#=6
#und jetzt kommt der Punkt wo Python merkt. OK noch eine Runde geht nicht, da der nächste Summand jetzt 6 wäre und 6> n.
#Jetzt würde Python 2+4+6 = 12 ausgeben. Die Richtige Rechnung wäre aber 2 + 4 = 6.
# Die Summen werden im Hintergrund gespeichert und am Ende aufsummiert. Deswegen haben wir wenn wir zuerst erhöhemn eine Summe zu viel.
#i+= 2 bedeutet wir starten mit 0 + 2= 2 (Erste Summe die im Hintergrund gepeichert wird.) dann geht es zur nächsten Runde i+= 2 + summe = summe + 2 (Also die schon gespeicherte Summe + 2)
# die nächste Summe wäre dann 4. Und da 4 <= 4 ist startet python die nächste Runde und rechnet nochmal i+= 2 + vorherige Summe aus Runde 2 welche 4 ist + 2) Die 3te Summe ist
#nun 6 und Python checkt. Ok wir erfüllrn nicht mehr die Bedingung für n, wir müssen Schleife stoppen. Da aber schon Summe 1 = 2, Summe 2= 4 und nun Summe 3= 6 ist bekommen wir fälschlicherweise 12 heraus. 
#machen wir aber erst die Addition und erhöhen dann läuft es so ab das python wieder startet bei summe = 0 und i= 0 und dann geht die erste Runde los i+=2 + summe = summe(0) + 2 was die erste zu speichernde 
#Summe ergibt danach gehen wir in Runde 2 : i+=2 + summe = summe(2) + 2 = 4 da wir in der nächsten Runde vor der Erhöhung addieren merkt python das summe+= 4 der letzte gerade Wert <= n ist und stoppt die Schleife.
"""
"""
n = int(input("Bitte gib eine Zahl ein:"))

summe = 0
i=0

while i <= n:

    summe += i
    i+= 2

print("Hier ist die Summe aller geraden Zahlen <=" ,n, "ist" ,summe ,":")

"""
"""
n = int(input("Bitte gib hier deine Zahl ein:"))

summe = 0
i = 1

while i <= n:
    summe+= i
    i += 2

print("Die Summe der ungerade Zahlen <=" ,n, "ist" ,summe,":")
"""
"""
n = int(input("n eingeben:"))

summe = 0
i = 0
while i <= n:
    if i % 3 != 0:
        summe += i
    i += 1
print("Summe =" , summe)
"""

n= int(input("n eingeben:"))

summe = 0
i = 2
teile = []
while i<= n:

    if i % 2 ==0:
        summe += i
        teile.append(str(i))

    i += 3

ausdruck = "+ ".join(teile)

print(f"{ausdruck} = {summe}")

n = int(input("n eingeben:"))

summe = 0
i = 2

teile=[]

while i <= n:
    summe+= i
    teile.append(str(i))
    i += 3

ausdruck = "+".join(teile)

print(f"{ausdruck} = {summe}")


n = int(input("n eingeben"))

summe = 0
i = 2

teile = []

while i <=n:
    if i % 4  != 0:
        summe += i
        teile.append(str(i))
    i+=2
ausdruck = "+".join(teile)

print (f"{ausdruck} = {summe}")


summe = 0
i = 1
count = 0

teile=[]

while count <= 7:
    summe += i
    teile.append(str(i))
    count += 3
ausdruck = "," .join(teile)

print(f"{ausdruck} = {summe}")


i = 0
teile=[]
summe = 0

while i <= 50:
    
if qs % 2 != 0:
    teile.append(str(i))
    summe+=1
i+= 1

ausdruck ="+".join(teile)

print(f"{ausdruck} = {summe}")









