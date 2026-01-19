#!/usr/bin/env python3
import random
optionen = ["Schere", "Stein", "Papier"] #Hier werden Stringoptionen für beide Spieler erzeugt

meine_eingabe = input("Schere, Stein, Papier?") #Spieler 1 wird gefragt, ob Stein .....
print(meine_eingabe)

#zufallszahl = random.randint(0, 3) #random.randint(0, 3) 0==Schere 1==Stein 2==Papier
computer = random.choice(optionen) #hier bekommt der Computer den Befehl sich Random eine der oben genannten Optionen auszusuchen


print("Computer wählt", computer) 

if meine_eingabe == computer: # If bedingung für unentschieden
    print("Unentschieden")
elif ( (meine_eingabe == "Schere" and computer == "Papier") #elif bedingungen für Bens Siegeszug
    or (meine_eingabe == "Papier" and computer == "Stein") 
    or (meine_eingabe == "Stein" and computer == "Schere")):
    print("Gewinner ist Ben")
else:
    print("Gewinner ist Computer") #Bei allen anderen Sachen gewinnt Computer







