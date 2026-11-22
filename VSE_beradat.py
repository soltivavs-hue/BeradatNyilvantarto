class VSE_Dolgozo:
    def __init__(self, nev, torzsszam, alapber, ledolgozott, tavollet):
        self.nev = nev
        self.torzsszam = torzsszam
        self.alapber = alapber
        self.ledolgozott = ledolgozott
        self.tavollet = tavollet

    def adatok(self):
        return f"{self.nev} | {self.torzsszam} | {self.alapber} Ft | {self.ledolgozott} nap | {self.tavollet} nap"