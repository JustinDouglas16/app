class auto:
    def __init__(self, kleur, merk, bouwjaar, snelheid):
        self.kleur = kleur
        self.merk = merk
        self.bouwjaar = bouwjaar
        self.snelheid = 0
    # methods voor rijden van een auto
    def rijden(self):
        print("Deze auto met een", self.kleur, "kleur rijd heel snel weg met een snelheid van ", self.snelheid," km/h !")
    # methods voor toeteren van een auto
    def toeteren(self):
        print("deze auto", self.merk, "kan iedereen verslaan!")
    # methods voor remmen van een auto
    def remmen(self):
        print("deze stoere auto met een", self.bouwjaar, "kleur en merk van", self.merk, "kan slecht remmen")
    def gas(self):
        self.snelheid += 5
    def rem(self):
        self.snelheid -= 5
    def get_snelheid(self):
        return self.snelheid
# de properties van een python slang
nighr_rider = auto("blauw", "tuit", "boom", 0)
nighr_rider.rijden()
nighr_rider.gas()
nighr_rider.rijden()
nighr_rider.gas()
nighr_rider.gas()
nighr_rider.rijden()
nighr_rider.toeteren()
nighr_rider.remmen()
nighr_rider.gas()

