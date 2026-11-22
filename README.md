# Béradat-nyilvántartó

**Hallgató:** Varga-Solti Éva  
**Tantárgy:** Szkript nyelvek  
**Programozási nyelv:** Python

## A feladat rövid leírása

A Béradat-nyilvántartó egy egyszerű, Tkinterrel készített grafikus alkalmazás, amellyel dolgozók alapadatait és bérhez kapcsolódó adatait lehet rögzíteni. A program kezeli a dolgozó nevét, törzsszámát, havi alapbérét, ledolgozott napjait és távolléti napjait.

A felhasználó új dolgozót vehet fel, megtekintheti a dolgozók listáját, törölheti a kijelölt dolgozót, valamint szövegfájlba mentheti az adatokat. Indításkor a program megpróbálja betölteni a korábban elmentett adatokat.

A bevitt mezőket a program ellenőrzi: minden mező kitöltése szükséges, a bér és a napok egész számok lehetnek, a bérnek pozitívnak, a napoknak nemnegatívnak kell lenniük.

## A projekt fájljai

- `main.py` – a grafikus felület, az eseménykezelés, az adatrögzítés és a fájlkezelés.
- `VSE_beradat.py` – a saját modul, amely a `VSE_Dolgozo` osztályt tartalmazza.
- `dolgozok.txt` – a program által használt, helyi szöveges adatfájl.

## Felhasznált modulok

| Modul | Szerepe |
| --- | --- |
| `tkinter` | Grafikus felület: ablak, címkék, beviteli mezők, lista és gombok. |
| `tkinter.messagebox` | Hibaüzenetek megjelenítése. |
| `random` | Véletlenszerű bemutató azonosító előállítása. |
| `VSE_beradat` | Saját modul a dolgozó adatainak kezelésére. |

A bemutatandó `random` modul három felhasznált függvénye:

- `random.randint(100, 999)` – véletlen egész számot generál.
- `random.choice(["A", "B", "C"])` – véletlenszerűen kiválaszt egy betűt.
- `random.uniform(1, 9)` – véletlen valós számot generál, amelyet a program egy tizedesre kerekít.

Az így létrejövő azonosító bemutató célú, egyedisége nem garantált.

## Saját osztály és függvények

**Saját osztály:** `VSE_Dolgozo` – tárolja a dolgozó nevét, törzsszámát, alapbérét, ledolgozott és távolléti napjait. Az `adatok()` metódus megjeleníthető szöveggé alakítja ezeket az adatokat.

**Saját függvények a `main.py` fájlban:**

- `VSE_rogzites()` – beolvassa és ellenőrzi a mezőket, létrehoz egy `VSE_Dolgozo` objektumot, majd a listába helyezi az adatokat.
- `VSE_torles()` – törli a kijelölt dolgozót, majd menti a listát.
- `VSE_mentes()` – a lista tartalmát a `dolgozok.txt` fájlba menti.
- `VSE_betoltes()` – induláskor betölti a korábbi adatokat, ha létezik a fájl.

## Grafikus felület és eseménykezelés

A grafikus felület `tkinter` használatával készült. A „Dolgozó rögzítése”, „Kijelölt törlése” és „Adatok mentése” gombokhoz a program a `command` paraméterrel rendel függvényeket. A hibás adatbevitelről `messagebox.showerror()` tájékoztatja a felhasználót.

## Futtatás

1. A `main.py` és a `VSE_beradat.py` fájl kerüljön ugyanabba a mappába.
2. Indítsuk el a `main.py` fájlt Python 3-mal, például PyCharmban.
3. Töltsük ki a mezőket, majd kattintsunk a „Dolgozó rögzítése” gombra.
4. A mentéshez kattintsunk az „Adatok mentése” gombra. Az adatok a `dolgozok.txt` fájlba kerülnek.

A program a Python szabványos moduljait használja, ezért nem szükséges külön csomagot telepíteni.

