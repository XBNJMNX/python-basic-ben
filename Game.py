seltenheit = "legendary"
glueck = 9
vip = True
if seltenheit == "legendary" and glueck >= 100 and vip:
    print("Aus der Hölle krank dikka")
elif seltenheit == "epic" and glueck < 100 and glueck >= 75 and not vip:
    print ("Auf dem besten Weg zum Vip Member. Ganz großes Kino")
elif seltenheit == "rare" and glueck < 75 and glueck >= 50 or vip:
    print ("Not Bad")
elif seltenheit == "legendary" and glueck < 50 and glueck > 30 and vip:
    print("legendary Modus aber man kann nicht immer Punkten")
elif seltenheit == "beginner" and glueck > 30 and glueck > 10 and vip:
    print ("Guter Start kleiner Padawan")
elif seltzenheit == "beginner" and glueck <=10 or vip:
    ("Guter Einstieg. Übung macht den Meister")
else:
    print ("Schrott")