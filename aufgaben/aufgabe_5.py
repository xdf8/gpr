# 5a)
# Programmiere selbst eine solche Funktion str_count(string, pattern),
# die zählt, wie oft pattern in string enthalten ist.
# Verwende für diese Aufgabe keine String-Operationen ausser Indexierung,
# Slicing und Vergleichen. Ausserdem darfst Du die Funktion len benutzen,
# damit Dein Programm die Länge der Strings herausfinden kann.

def str_count(string, pattern):
    count = 0
    for i in range(len(string)):
        if string[i:i+len(pattern)] == pattern:
            count += 1
    return count

print(str_count('abcabcabc', 'abc'))

# 5b)
# Programmiere noch eine andere Zählfunktion str_count_any(string, pattern),
# die den zweiten Parameter als Menge einzelner Zeichen interpretiert und zählt,
# wie viele Zeichen des ersten Parameter-Strings irgendeinem Zeichen dieser
# Menge entsprechen.

def str_count_any(string, pattern):
    count = 0
    for i in range(len(string)):
        if string[i] in pattern:
            count += 1
    return count

print(str_count_any('Das ist ein netter Versuch', 'er'))