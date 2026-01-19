temp = 10
bewegung = True
tuer_offen = True
if temp >= 10 and  tuer_offen and bewegung:
    print("Alarm Eindriingling oder irgendetwas stimmt nicht")
elif temp>= 10 and not tuer_offen and bewegung:
    ("Alles safe")
elif tuer_offen and not bewegung:
    print("Haben wir Säcke vor den Türen")
else:
    print ("Alles ruhig") 


