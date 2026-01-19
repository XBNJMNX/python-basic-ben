bewegung = False
tuer_offen = False
fenster_offen = False
alarm_scharf = True
temp = 21
if bewegung and (tuer_offen or fenster_offen) and alarm_scharf:
    print ("Alarm! Eindringling eleminieren")
elif alarm_scharf and not (tuer_offen and fenster_offen and bewegung) and 10<= temp <= 22:
    print ("Alarm scharf niemand zu Hause, nicht lüften")
elif not alarm_scharf and bewegung and not (tuer_offen and fenster_offen):
    print ("Alarm aus, Bewohner zu Hause")
elif not bewegung and not alarm_scharf and (tuer_offen or fenster_offen) and temp < 10:
    print ("Es ist kalt! Bitte Fenster schließen!")
elif not bewegung and not alarm_scharf and not (tuer_offen and fenster_offen) and 10<= temp <= 22:
    print ("Temperatur top, kein Lüften nötig")
elif  bewegung and not alarm_scharf and not (tuer_offen and fenster_offen) and 10<= temp <= 22:
    print ("Temperatur top, kein Lüften nötig")
elif not bewegung and alarm_scharf and not (tuer_offen and fenster_offen) and temp > 22:
    print ("Alarm scharf! Temperatur zu warm, Lüften nötig! Bitte Fenster öffnen")
elif bewegung and not (fenster_offen and tuer_offen and alarm_scharf):
    print ("Alles cool")
else:
    print ("Sytem macht keine Meldung")











