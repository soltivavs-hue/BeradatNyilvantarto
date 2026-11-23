
import tkinter as tk
from tkinter import messagebox
import random
from VSE_beradat import VSE_Dolgozo


def VSE_azonosito():
    szam = random.randint(100, 999)
    betu = random.choice(["A", "B", "C"])
    ellenorzo = round(random.uniform(1, 9), 1)
    return f"{betu}{szam}-{ellenorzo}"


class VSE_BeradatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Béradat-nyilvántartó")
        self.root.geometry("850x650")

        tk.Label(root, text="BÉRADAT-NYILVÁNTARTÓ", font=("Arial", 18)).pack(pady=20)

        self.nev_mezo = self.VSE_mezo("Dolgozó neve:")
        self.torzsszam_mezo = self.VSE_mezo("Törzsszám:")
        self.alapber_mezo = self.VSE_mezo("Havi alapbér (Ft):")
        self.ledolgozott_mezo = self.VSE_mezo("Ledolgozott napok:")
        self.tavollet_mezo = self.VSE_mezo("Távolléti napok:")

        tk.Button(root, text="Dolgozó rögzítése", command=self.VSE_rogzites).pack(pady=10)

        self.dolgozo_lista = tk.Listbox(root, width=110, height=6)
        self.dolgozo_lista.pack(pady=5)

        tk.Button(root, text="Kijelölt törlése", command=self.VSE_torles).pack(pady=5)
        tk.Button(root, text="Adatok mentése", command=self.VSE_mentes).pack(pady=5)

        self.root.bind("<Return>", lambda event: self.VSE_rogzites())
        self.dolgozo_lista.bind("<Delete>", lambda event: self.VSE_torles())

        self.VSE_betoltes()

    def VSE_mezo(self, felirat):
        tk.Label(self.root, text=felirat).pack()
        mezo = tk.Entry(self.root, width=40)
        mezo.pack(pady=5)
        return mezo

    def VSE_rogzites(self):
        mezok = [self.nev_mezo, self.torzsszam_mezo, self.alapber_mezo,
                 self.ledolgozott_mezo, self.tavollet_mezo]
        nev, torzsszam, alapber, ledolgozott, tavollet = [m.get().strip() for m in mezok]

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
        self.dolgozo_lista.insert(tk.END, f"{dolgozo.adatok()} | Azonosító: {VSE_azonosito()}")

        for mezo in mezok:
            mezo.delete(0, tk.END)

    def VSE_torles(self):
        kijelolt = self.dolgozo_lista.curselection()
        if kijelolt:
            self.dolgozo_lista.delete(kijelolt[0])
            self.VSE_mentes()

    def VSE_mentes(self):
        with open("dolgozok.txt", "w", encoding="utf-8") as fajl:
            for dolgozo in self.dolgozo_lista.get(0, tk.END):
                fajl.write(dolgozo + "\n")

    def VSE_betoltes(self):
        try:
            with open("dolgozok.txt", "r", encoding="utf-8") as fajl:
                for dolgozo in fajl:
                    if dolgozo.strip():
                        self.dolgozo_lista.insert(tk.END, dolgozo.strip())
        except FileNotFoundError:
            pass


root = tk.Tk()
app = VSE_BeradatApp(root)
root.mainloop()
