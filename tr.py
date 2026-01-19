#!/usr/bin/env python3
import math
zahl_1 = input("Bitte gib die erste Zahl ein:")
zahl_1 = float (zahl_1)
zahl_2 = float (input ("Bitte gib die zweite Zahl ein:"))

operation = input ("Bitte gib eins der Rechenzeichen (+, -, /, *, **, sqrt) ein")
if operation == "+":
  ergebnis = zahl_1 + zahl_2
elif operation == "-":
  ergebnis = zahl_1 - zahl_2
elif operation == "/":
  ergebnis = zahl_1 / zahl_2
elif operation == "*":
  ergebnis = zahl_1 * zahl_2
elif operation == "**":
  ergebnis = zahl_1 ** zahl_2
elif operation == "sqrt":
  ergebnis = math.sqrt (zahl_1)

else:
  print("Leider ungültige Eingabe") 


print ("Das Ergebnis deiner Aufgabe ist" , ergebnis)
