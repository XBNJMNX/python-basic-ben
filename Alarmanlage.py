bewegung = True
tuer = True
fenster = True
if bewegung and tuer or fenster:
    print ("Alarm Eindringling oder etwas stimmt nicht!")
elif not bewegung and tuer or Fenster:
    print ("Tür oder Fenster schließen")
elif not bewegung and not (tuer and  Fenster):
    ("Alles sicher. Eventuell lüften")
elif not bewegung and not tuer and fenster:
    print ("Fenster schließen")
elif bewegung and tuer and not fenster:
    print ("Checken wer da ist")
elif bewegung and not (tuer and fenster):
    print ("Jemand ist innerhalb in der Nähe der Tür")
elif bewegung and not tuer and fenster:
    print ("Fenster schließen")
elif not bewegung and tuer and not fenster:
    print ("Tür schließen")




