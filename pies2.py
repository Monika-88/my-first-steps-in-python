class Pies2:

    gatunek = 'pies domowy'

    def __init__(self,rasa,imie,wiek):
        print('wewnatrz metody init')
        self.rasa = rasa
        self.imie = imie
        self.wiek = wiek
    def szczekaj(self):
        return ('Hau! Hau!')

    def zaprezentuj_psa(self):
        print('Rasa to' + self.rasa)
        print('Imie to ' + self.imie)
        print('Wiek psa to ' + str(self.wiek))


reksio = Pies2('kundelek','Reksio',2)
print(reksio.wiek)
reksio.wiek = 3
print(reksio.wiek)
print(reksio.gatunek)
Pies2.gatunek = 'Ptak'
print(Pies2.gatunek)
print(reksio.szczekaj())
print(reksio.zaprezentuj_psa())

