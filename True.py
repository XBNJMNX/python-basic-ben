bewegung = True
tuer_offen = False
if bewegung and not tuer_offen:
    print ("Alarm!")
elif not bewegung and not tuer_offen:
    print ("Sicher")
elif not bewegung and tuer_offen:
    print ("Tür zu!")
else:
    print("Alles OK!")