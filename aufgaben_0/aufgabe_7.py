# Um diese Aufgabe zu lösen, solltest Du mit Strings umgehen können,
# Operationen auf Strings wie strip, split und Slicing kennen.
# Programmiere eine Funktion, die einen als Argument angegebenen String zerlegt,
# der folgende Struktur hat: Zwei Zahlen, getrennt durch ein ‘-‘,
# nach einem Leerzeichnen ein einzelner Buchstabe gefolgt von einem Doppelpunkt
# und nach einem weiteren Leerzeichen beliebige Buchstaben bis zum String-Ende.
# Ein Beispiel könnte so aussehen: «32-165 k: sdklffs».
# Das Resultat der Zerlegung soll ein Tupel oder eine Liste sein mit den einzelnen
# Elementen aus dem String: (32, 165, "k", "sdklffs").

# n*-n* l: l*

def decompose_string(string):
    result = []
    # ':' entfernen, ist unwichtig
    string = string.replace(':', '') # geht auch ohne replace, nur mit splits
    result.append(string.split('-')[0])
    # da nur ein '-', wird der string immer zweigeteilt
    temp = string.split('-')[1]
    for i in temp.split(' '):
        result.append(i)
    return result

print(decompose_string(string = '32-165 k: sdklffs'))