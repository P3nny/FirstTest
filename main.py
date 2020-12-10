
'''
KEINE PANIK!
Ja, das ist eine Coding-Aufgabe für angehende Volontär*innen, aber kein Grund zur Panik. Die Übungen setzen kein Vorwissen voraus. Schritt für Schritt werden hier im Text Grundlagen der Programmiersprache Python erklärt. Mit den Übungen dazu möchten wir herausfinden, wie furchtlos ihr gegenüber technischen Herausforderungen seid. 
'''

print('00:')
print('Hello world!')
print('-------------')
print('\n')

'''
Was denkst du, was diese vier Zeilen Python-Code tun könnten?
Finde es heraus, indem Du auf den grünen 'Run'-Knopf oben in der Mitte des Fensters klickst. Dadurch wird der Code ausgeführt und das Ergebnis im schwarzen Fenster rechts angezeigt.
Die "print"-Zeilen sorgen dafür, dass die Texte und Zeichen in den Klammern im schwarzen Fenster "ausgedruckt" werden.
'''

'''
Übung:
Schreibe jetzt deine erste Zeile Code, die den Text "Hallo WDR" ausgibt, indem du diesen Code hier änderst: '''

print('Hallo WDR')

'''

'''

from datetime import date
heute = date.today()
print(heute)

# mit dem Datum lässt sich rechnen
geburtstag = date(1980,10,17)
heute = date.today()
alter = heute - geburtstag
print(alter.days, "Tage seit Geburt vergangen")

