#!/usr/bin/env python3
"""
def summen(a,b,c):
    return (a + b) %c
a = 2
b = 3
c = 5

print(summen(a,b,c))

def prüfung_groesser_kleiner(x,y):
    if x > y:
        return "x ist gößer als y"
    elif x == y:
        return "x ist gleich y"
    else:
        return "x ist kleiner als y"
print(prüfung_groesser_kleiner(2,2))

def zahlen_liste ():
    for i in range (1,6):
        print("Aktueller Wert" ,i)
(zahlen_liste())

def zaelen ():
    n = 10
    while n > 0:
        print("n ist" , n)
        n -= 1
(zaelen())

def alter_info (alter):
    jahre_bis_30 = 30 - alter
    
    if jahre_bis_30 > 0:
        return f" in {jahre_bis_30} Jahren wirst du 30"
    else:
        return "Du bist bereits 30 Jahre oder älter"

name = input("Bitte geben Sie ihren Namen ein ")
alter = int(input("Bitte geben Sie ihr Alter ein "))

info = alter_info(alter)

print(f"Hallo {name}, Du bist {alter} Jahre alt und {info}")
alter_info(alter)

def alter_info(alter):
    jahre_bin_50 = 50 - alter
    if jahre_bin_50 > 0:
        return f"in {jahre_bin_50} Jahren wirst du 50"
    else:
        return "Du bist bereits 50 oder älter"
name = input("Bitte gib deinen Namen ein ")
alter = int(input("Bitte gib dein Alter ein "))

info = alter_info(alter)
print(f"Dein Name ist {name} und du bist {alter} Jahre alt und {info}")

def lieblings(zahl):
    return lieblingszahl + 14.5

lieblingsfilm = input("Bitte geb deinen Lieblingsfilm ein ")
lieblingszahl = int(input("Bitte gib deine Lieblingszahlein "))

info = lieblings(lieblingszahl)
print(f"Dein Lieblingsfilm ist {lieblingsfilm} und deine lieblingszahl ist {lieblingszahl} diese mit 14,5 addiert ist {info}")
"""

import math
def taschenrechner ():

    operator = input("Bitte gib eines der Rechenzeichen ein (+, -, *, /, **, sqrt)")
    if operator == "sqrt":
        zahl_0 = float(input("Bitte gib eine Zahl ein " ))
        return math.sqrt(zahl_0)

    zahl_1 = float(input("Bitte gib die erste Zahl ein "))
    zahl_2 = float(input("Bitte gib die zweite Zahl ein "))

    if operator == "+":
        return zahl_1 + zahl_2
    elif operator == "-":
        return zahl_1 - zahl_2
    elif operator == "*":
        return zahl_1 * zahl_2
    elif operator == "/":
        return zahl_1 / zahl_2
    elif operator == "**":
        return zahl_1 ** zahl_2
    else:
        return"Leider ungültige Eingabe"
print("Ergebnis: ", taschenrechner ())

