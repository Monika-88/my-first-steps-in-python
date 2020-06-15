class Pies:

    gatunek = 'pies domowy'

    def __init__(self,rasa,imie,wiek):

        self.rasa = rasa
        self.imie = imie
        self.wiek = wiek

reksio = Pies('kundelek','Reksio',2)
print(reksio.wiek)
print(reksio.imie)
print(reksio.rasa)
print(reksio.gatunek)
print(Pies.gatunek)