#!/usr/bin/env python 3

name = input("Bitte geben Sie Ihren Namen ein:")
print ("Hallo," + name +"!")


alter = input ("Bitte geben Sie Ihr Alter ein:")
alter = int(alter)
print ("Sie sind"  , alter , "Jahre alt.")

jahre_bis_30  = 30 - alter
if jahre_bis_30 > 0:
  print("In " + str(jahre_bis_30) + " Jahren werden Sie 30")
else:
  print("Sie sind bereits über 30 Jahre alt:")

film = input ("Bitte gib deinen Lieblingsfilm ein:")
zahl = input ("Bitte gib deine Lieblingszahl ein:")
zahl = float(zahl) + 14.5
print ("Dein Lieblingsfilm ist" , film , "und deine Lieblingszahl + 14.5 ist" , zahl, "." )

getraenk = input ("Bitte gib dein Lieblingsgetränk ein:")
essen = input ("Bitte gib dein Lieblingsessen ein:")
sportart = input ("Bitte gib deine Lieblingssportart an:")
print ("Dein Lieblingsgetränk ist" , getraenk , ", dein Lieblingsessen ist" , essen, "und deine Lieblingssportart ist" , sportart,".")
if sportart == "Fußball":
  print("Ole Ole Ole Ole!")
elif sportart == "Basketball":
  print ("Time to jump up!")
elif sportart == "Football":
  print("Touchodown")
elif sportart == "Schwimmen":
  print ("Delfin im Tauchgang")
else:
  print ("Sehr interessant")





