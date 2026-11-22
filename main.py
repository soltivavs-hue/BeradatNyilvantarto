
import tkinter as tk
from tkinter import messagebox
import random
from VSE_beradat import VSE_Dolgozo


def VSE_rogzites():
    nev = nev_mezo.get().strip()
    torzsszam = torzsszam_mezo.get().strip()
    alapber = alapber_mezo.get().strip()
    ledolgozott = ledolgozott_mezo.get().strip()
    tavollet = tavollet_mezo.get().strip()

    if not nev or not torzsszam or not alapber or not ledolgozott or not tavollet:
        messagebox.showerror("Hiba", "Minden mezőt ki kell tölteni!")
        return

    try:
        alapber = int(alapber)
        ledolgozott = int(ledolgozott)
        tavollet = int(tavollet)
    except ValueError:
        messagebox.showerror("Hiba", "A bér és a napok csak egész számok lehetnek!")
        return

    if alapber <= 0 or ledolgozott < 0 or tavollet < 0:
        messagebox.showerror("Hiba", "Hibás bér vagy napok!")
        return

    dolgozo = VSE_Dolgozo(nev, torzsszam, alapber, ledolgozott, tavollet)

    szam = random.randint(100, 999)
    betu = random.choice(["A", "B", "C"])
    ellenorzo = round(random.uniform(1, 9), 1)

    azonosito = f"{betu}{szam}-{ellenorzo}"
    adat = f"{dolgozo.adatok()} | Azonosító: {azonosito}"

    dolgozo_lista.insert(tk.END, adat)

    nev_mezo.delete(0, tk.END)
    torzsszam_mezo.delete(0, tk.END)
    alapber_mezo.delete(0, tk.END)
    ledolgozott_mezo.delete(0, tk.END)
    tavollet_mezo.delete(0, tk.END)


def VSE_torles():
    kijelolt = dolgozo_lista.curselection()

    if kijelolt:
        dolgozo_lista.delete(kijelolt[0])
        VSE_mentes()


def VSE_mentes():
    with open("dolgozok.txt", "w", encoding="utf-8") as fajl:
        for dolgozo in dolgozo_lista.get(0, tk.END):
            fajl.write(dolgozo + "\n")


def VSE_betoltes():
    try:
        with open("dolgozok.txt", "r", encoding="utf-8") as fajl:
            for dolgozo in fajl:
                dolgozo_lista.insert(tk.END, dolgozo.strip())
    except FileNotFoundError:
        pass


root = tk.Tk()
root.title("Béradat-nyilvántartó")
root.geometry("850x650")

cimke = tk.Label(root, text="BÉRADAT-NYILVÁNTARTÓ", font=("Arial", 18))
cimke.pack(pady=20)

nev_cimke = tk.Label(root, text="Dolgozó neve:")
nev_cimke.pack()

nev_mezo = tk.Entry(root, width=40)
nev_mezo.pack(pady=5)

torzsszam_cimke = tk.Label(root, text="Törzsszám:")
torzsszam_cimke.pack()

torzsszam_mezo = tk.Entry(root, width=40)
torzsszam_mezo.pack(pady=5)

alapber_cimke = tk.Label(root, text="Havi alapbér (Ft):")
alapber_cimke.pack()

alapber_mezo = tk.Entry(root, width=40)
alapber_mezo.pack(pady=5)

ledolgozott_cimke = tk.Label(root, text="Ledolgozott napok:")
ledolgozott_cimke.pack()

ledolgozott_mezo = tk.Entry(root, width=40)
ledolgozott_mezo.pack(pady=5)

tavollet_cimke = tk.Label(root, text="Távolléti napok:")
tavollet_cimke.pack()

tavollet_mezo = tk.Entry(root, width=40)
tavollet_mezo.pack(pady=5)

rogzites_gomb = tk.Button(root, text="Dolgozó rögzítése", command=VSE_rogzites)
rogzites_gomb.pack(pady=10)

dolgozo_lista = tk.Listbox(root, width=110, height=6)
dolgozo_lista.pack(pady=5)

torles_gomb = tk.Button(root, text="Kijelölt törlése", command=VSE_torles)
torles_gomb.pack(pady=5)

mentes_gomb = tk.Button(root, text="Adatok mentése", command=VSE_mentes)
mentes_gomb.pack(pady=5)

VSE_betoltes()

root.mainloop()
