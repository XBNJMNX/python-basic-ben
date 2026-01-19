#!/usr/bin/env python 3
"""
n = input ("Name")
a = int(input("Alter"))
g = float(input("Gewicht"))
gr = float(input("Größe"))
ge = (input("Geschlecht"))

print ("\nMiniprofil")
print (f"{n} ist {a} Jahre alt {ge}, wiegt {g} kg und ist {gr}m groß")

if   1.5 < gr < 1.6 and g >= 70 and ge == "weiblich":
    print("Bitte Ernährung anpassen. Das Gewicht sollte runter!")
elif 1.65 <= gr < 1.8 and 70 <= g <=75 and ge == "männlich":
    print ("Alles in Ordnung!")
elif 1.7 < gr < 1.8 and g <= 75 and ge == "weiblich":
    print ("Alles supi!")
elif 1.8 < gr < 1.9 and 80 < g <= 90 and ge == "männlich":
    print ("Alles im Rahmen")
else :
   print ("Ist nur eine Übung, Gewichte und Größen können wahrscheinlich besser in einer toolen Funktion analysiert werden")

ld = []

ls = input ("Lieblingssport:")
le = input ("Lieblingsessen:")
lt = input ("Lieblingstier:")
lz = input ("Lieblingszahl")

ld.append (ls)
ld.append (le)
ld.append (lt)
ld.append (lz)

print ("\n Meine Lieblingsdinge")
for i in range (len(ld)):
    
    
    print (f"{i + 1}: {ld [i]}")
"""
"""
b = False
to = True
fo = True
As = True
temp = float(12)                                        #Bei den True False haben wir immer 2^n Möglichkeiten 
lf = float(49.5)                                        # Man könnte hier 2^4 Möglichkeiten wählen, aber meist machen nur einige Sinn
                                                        # Die Zuweisungen sind wie Sensoren die aber in Python manuell gesteuert werden.
if not b and As and (to or fo):                         # Für Sensorik bräuchte man die entsprechende Hardware.
    print ("Eindringling Alarm")
elif b and not (to and fo) and temp > 10:
    print ("Alles sicher, Heizung an")
elif not b and not (to and fo) and temp > 10:
    print ("Alles sicher, Heizung an")
elif b and not (to and fo) and  10 < temp < 20:
    print ("Alles sicher, Temperatur top")
elif not b and not (to and fo) and temp >= 20:
    print ("Alles sicher, Heizung aus")
elif not b and not to and fo and temp < 10:
    print ("Fenster automatisch schließen")
elif As and not b and not (to and fo):
    print("Alarm scharf, Nachtmodus")
elif not As and b and not to and fo:
    print ("Alarm aus Tagmodus, Bewohner zu Hause")
elif b and (to and fo) and lf > 60:
    print ("Luftentfeuchter an")
elif b and (to and fo) and lf <= 60:
    print ("Luftentfeuchter aus")
elif not b and (to and fo) and lf > 60:
    print ("Luftentfeuchter an")
elif not b and (to and fo) and lf <= 60:
    print ("Luftentfeuchter aus")
else:
    print("Alle ok")
"""
"""
def smart_home(b, As, fo, to, temp, lf):
                                         #Wir definieren eine Funktion mit def


 # Alarmeinstellungen
    if not b and As and (to or fo):                        
        print ("Alarm")
    elif b and (to or fo) and As:
        print ("Eindringling Alarm")
    elif b and to and fo and not As:
        print ("Alles gut!")
    elif not b and not (to and fo and As):
        print("Alles gut!")
# Klima Einstellungen
    if 20<= temp <= 70 and 60 <= lf <= 100 and not fo:
        print("Fenster auf und Luftentfeuchter an!")
    elif 20 <= temp <= 70 and 0 <= lf <= 59.9 and not fo:
        print ("Fenster auf und Luftentfeuchter aus!")
    elif 0 <= temp <= 19.9 and 0 <= lf <= 59.9 and fo:
        print ("Fenster zu und Luftentfeuchter aus!")
    elif 0 <= temp <= 19.9 and 60 <= lf <= 100 and not fo:
        print("Fenster zu und Lutentfeuchter an!")
    else:
        print ("System erkennt kein Problem")
b = False
As = True
fo = True
to = False
temp = 5.34
lf = 45
smart_home (b, As, fo, to, temp, lf)    #Wichtig damit die Python weiß das es jetzt mit der Funktion starten kann

"""

def smart_home(b, As, fo, to, temp, lf):                                        


 # Alarmeinstellungen
    if not b and As and (to or fo):                        
        print ("Alarm")
    elif b and (to or fo) and As:
        print ("Eindringling Alarm")
    elif b and to and fo and not As:
        print ("Alles gut!")
    elif not b and not (to and fo and As):
        print("Alles gut!")
# Klima Einstellungen
    if 20<= temp <= 70 and 60 <= lf <= 100 and not fo:
        print("Fenster auf und Luftentfeuchter an!")
    elif 20 <= temp <= 70 and 0 <= lf <= 59.9 and not fo:
        print ("Fenster auf und Luftentfeuchter aus!")
    elif 0 <= temp <= 19.9 and 0 <= lf <= 59.9 and fo:
        print ("Fenster zu und Luftentfeuchter aus!")
    elif 0 <= temp <= 19.9 and 60 <= lf <= 100 and not fo:
        print("Fenster zu und Lutentfeuchter an!")
    else:
        print ("System erkennt kein Problem")
# Eingaben manuell für User und Sensorik
b = input ("Bewegung? True/False:")
As = input ("Alarm scharf? True/False:")
fo = input ("Fenster offen True/False:")
to = input ("Tür offen True/False:")
temp = float(input("Temperatur eingeben:"))
lf = float(input("Luftfeuchtigkeit eingeben:"))

# strip, lower und replace funktionieren wunderbar wenn der User einfach irgendwie das Wort eintippt. Unabhängig von Groß- u. Kleinschreibung und Leerzeichen.

b = b.strip().lower().replace(" " , " ") == "true"      #Hier kann man entweder Klammern nach dem = und hinter dem True machen oder man läasst sie weg. Beides geht es muss nur einheitlich sein.
As = As.strip().lower().replace(" " ," ") == "true"
fo = fo.strip().lower().replace(" " , " ") == "true"
to = to.strip().lower().replace(" " , " ") == "true"

smart_home(b, As, fo, to, temp, lf)





    








