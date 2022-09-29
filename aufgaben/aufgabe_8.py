# Programmiere eine Funktion,
# die für eine als Argument angegebene Zahl N eine Liste
# aller Zahlen i produziert,
# für die gilt 0 ≤ i < N und i**2 mod 5 = 4.


def ayylmao(n):
    result = []
    for i in range(n):
        if i**2 % 5 == 4:
            result.append(i)
    return result

print(ayylmao(10))