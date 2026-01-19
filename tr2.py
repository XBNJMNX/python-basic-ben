#!/usr/bin/env python 3
import math
zahl_1 = input("Bitte gib eine Zahl ein:")
zahl_1 = float (zahl_1)
zahl_2 = float (input("Bitte gib die zweite Zahl ein:"))

operation = input ("Bitte gib eines dieser Rechenzeichen ein: +, -, /, *, **: " )

if  operation == "+":
    ergebnis = zahl_1 + zahl_2
elif operation == "-":
    ergebnis = zahl_1 - zahl_2
elif operation == "/":
    ergebnis = zahl_1 / zahl_2
elif operation == "*":
    ergebnis = zahl_1 * zahl_2
elif operation == "**":
    ergebnis = zahl_1 ** zahl_2

else:
    print("Leider ungültige Eingabe")

print("Das Ergebnis ist" , ergebnis)

