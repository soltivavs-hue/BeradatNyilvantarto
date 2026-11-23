# Béradat-nyilvántartó

**Hallgató:** Varga-Solti Éva  
**Tantárgy:** Szkript nyelvek  
**Programozási nyelv:** Python

## A feladat rövid leírása

A Béradat-nyilvántartó egy egyszerű, Tkinterrel készített grafikus alkalmazás, amellyel dolgozók alapadatait és bérhez kapcsolódó adatait lehet rögzíteni. A program kezeli a dolgozó nevét, törzsszámát, havi alapbérét, ledolgozott napjait és távolléti napjait.

A felhasználó új dolgozót vehet fel, megtekintheti a dolgozók listáját, törölheti a kijelölt dolgozót, valamint szövegfájlba mentheti az adatokat. Indításkor a program megpróbálja betölteni a korábban elmentett adatokat.

A bevitt mezőket a program ellenőrzi: minden mező kitöltése szükséges, a bér és a napok egész számok lehetnek, a bérnek pozitívnak, a napoknak nemnegatívnak kell lenniük.

## A projekt fájljai

- `main.py` – a program indítása, a grafikus felület, az eseménykezelés, az adatrögzítés és a fájlkezelés.
- `VSE_beradat.py` – a saját modul, amely a `VSE_Dolgozo` osztályt tartalmazza.
- `dolgozok.txt` – a program által használt, helyi szöveges adatfájl.

## Modulok és a modulokban használt függvények

**Tanult modul – `tkinter`** (grafikus felület)

- `tk.Tk()` – az alapablak (`root`) létrehozása
- `title()`, `geometry()` – ablakcím és méret
- `tk.Label()`, `tk.Entry()`, `tk.Button()`, `tk.Listbox()` – felületi elemek
- `pack()` – elemek elhelyezése
- `get()`, `delete()`, `insert()`, `curselection()` – mezők és lista kezelése
- `bind()` – billentyűesemények hozzárendelése
- `mainloop()` – az eseménykezelő ciklus indítása
- `messagebox.showerror()` – hibaüzenet megjelenítése

**Bemutatandó modul – `random`**

- `random.randint(100, 999)` – véletlen egész számot generál
- `random.choice(["A", "B", "C"])` – véletlenszerűen kiválaszt egy betűt
- `random.uniform(1, 9)` – véletlen valós számot generál, amelyet a program egy tizedesre kerekít

A három függvényből a `VSE_azonosito()` állít elő bemutató célú azonosítót (egyedisége nem garantált).

**Saját modul – `VSE_beradat`**

- `VSE_Dolgozo` osztály, `adatok()` metódus

**Fájlkezelés (beépített)**

- `open()`, `write()` – adatok mentése és betöltése a `dolgozok.txt` fájlból

## Saját függvény és osztályok

**Saját függvény:** `VSE_azonosito()` – a `random` modul három függvényével azonosítót állít elő.

**Saját osztályok:**

- `VSE_Dolgozo` (a `VSE_beradat.py` modulban) – tárolja a dolgozó nevét, törzsszámát, alapbérét, ledolgozott és távolléti napjait. Az `adatok()` metódus megjeleníthető szöveggé alakítja ezeket.
- `VSE_BeradatApp` (a `main.py` fájlban) – a program ablakát és működését megvalósító osztály. Metódusai:
  - `VSE_mezo()` – címkét és beviteli mezőt hoz létre
  - `VSE_rogzites()` – beolvassa és ellenőrzi a mezőket, létrehoz egy `VSE_Dolgozo` objektumot, majd a listába teszi
  - `VSE_torles()` – törli a kijelölt dolgozót, majd menti a listát
  - `VSE_mentes()` – a lista tartalmát a `dolgozok.txt` fájlba menti
  - `VSE_betoltes()` – induláskor betölti a korábbi adatokat, ha létezik a fájl

## Program felépítése

- Indítás: `main.py`
- Alapablak: `root = tk.Tk()`
- Programnév: `app = VSE_BeradatApp(root)`

## Grafikus felület és eseménykezelés

A grafikus felület `tkinter` használatával készült. A „Dolgozó rögzítése”, „Kijelölt törlése” és „Adatok mentése” gombokhoz a program a `command` paraméterrel rendel metódusokat. A `bind()` segítségével az Enter billentyű is rögzíti a dolgozót, a listában kijelölt sor pedig a Delete billentyűvel is törölhető. A hibás adatbevitelről `messagebox.showerror()` tájékoztatja a felhasználót.

## Futtatás

1. A `main.py` és a `VSE_beradat.py` fájl kerüljön ugyanabba a mappába.
2. Indítsuk el a `main.py` fájlt Python 3-mal, például PyCharmban.
3. Töltsük ki a mezőket, majd kattintsunk a „Dolgozó rögzítése” gombra (vagy nyomjunk Entert).
4. A mentéshez kattintsunk az „Adatok mentése” gombra. Az adatok a `dolgozok.txt` fájlba kerülnek.

A program a Python szabványos moduljait használja, ezért nem szükséges külön csomagot telepíteni.

