"""
Olvasd be a konyvek.txt adatait, majd oldd meg az alábbi feladatokat!

1. Hány könyv szerepel a fájlban?
2. Melyik könyvnek van a legtöbb oldala?
3. Melyik könyvnek van a legkevesebb oldala?
4. Melyik szerző írt a legtöbb könyvet?
5. Átlagosan hány oldalasak a könyvek?

***EXTRA - nehezebb feladat*** (nem kötelező, de érdemes megpróbálni):
6. Melyik kiadó adott ki a legtöbb könyvet?

A megoldott feladatokat a kiirt_adatok nevű mappában hozd létre statisztika.txt néven!
"""

konyvek = []
with open('beolvasando_adatok/konyvek.txt', 'r', encoding='utf-8') as f:
    next(f)
    for sor in f:
        adatok = sor.strip().split(';')
        konyv = {'cím': adatok[0], 'szerző': adatok[1], 'oldalszám': int(adatok[2]), 'kiadó': adatok[3]}
        konyvek.append(konyv)

def legtobb(adat: str):
    vizsgalando = konyvek[0]
    for konyv in konyvek:
        if konyv[adat] > vizsgalando[adat]:
            vizsgalando = konyv
    return vizsgalando["cím"]

def legkevesebb(adat: str):
    vizsgalando = konyvek[0]
    for konyv in konyvek:
        if konyv[adat] < vizsgalando[adat]:
            vizsgalando = konyv
    return vizsgalando["cím"]

#1.feladat
komyvek_szama = len(konyvek)

#2.feladat
leghosszabb_konyv = legtobb("oldalszám")

#3.feladat
legrovidebb_konyv = legkevesebb("oldalszám")

#4.feladat
legtobb_konyvet_iro = legtobb("szerző")

#5.feladat
osszes_oldal = 0
for konyv in konyvek:
    osszes_oldal += konyv["oldalszám"]
    atlag_oldal = osszes_oldal/komyvek_szama

#6.feladat
legtobb_konyvet_kiado = legtobb("kiadó")


print(f"1. A beolvasott fájlban összesen {komyvek_szama} könyv szerepel.")
print(f"2. A legtöbb oldalas könyv: {leghosszabb_konyv}.")
print(f"3. A legkevesebb oldalas könyv: {legrovidebb_konyv}.")
print(f"4. A legtöbb könyvet író szerző: {legtobb_konyvet_iro}.")
print(f"5. Az átlagos oldalszám: {atlag_oldal:.0f}. ")
print(f"***A legtöbb könyvet kiadó kiadó: {legtobb_konyvet_kiado}.")


with open('kiirt_adatok/statisztika.txt', 'w', encoding='utf-8') as c:
    c.write(f"1. A beolvasott fájlban összesen {komyvek_szama} könyv szerepel.\n")
    c.write(f"2. A legtöbb oldalas könyv: {leghosszabb_konyv}.\n")
    c.write(f"3. A legkevesebb oldalas könyv: {legrovidebb_konyv}.\n")
    c.write(f"4. A legtöbb könyvet író szerző: {legtobb_konyvet_iro}.\n")
    c.write(f"5. Az átlagos oldalszám: {atlag_oldal:.0f}.\n")
    c.write(f"***A legtöbb könyvet kiadó kiadó: {legtobb_konyvet_kiado}.\n")