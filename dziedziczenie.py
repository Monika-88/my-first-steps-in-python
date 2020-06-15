class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "Nazywam sie " + self.imie + " " + self.nazwisko

class Student(Osoba):

    def __init__(self,imie,nazwisko,numer_indeksu):
        Osoba.__init__(self,imie,nazwisko)
        self.indeks = numer_indeksu

    def podaj_numer_indeksu(self):
        return self.indeks

    def przedstaw_sie(self):
        return "Jestem studentem i nazywam się " + self.imie

# student = Student('Tomasz','Kot',123456)     #1
# print(student.przedstaw_sie())
# print(student.podaj_numer_indeksu())

osoba = Osoba('Tomasz','Kot')     #2
print(osoba.przedstaw_sie())
#print(student.podaj_numer_indeksu())
