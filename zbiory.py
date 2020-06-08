pierwszy_zbior = {"Warszawa", "Kraków", "Katowice", "Lodz"}
drugi_zbior= {"Warszawa"}

print(pierwszy_zbior)
pierwszy_zbior.add("Kielce")
print(pierwszy_zbior)
pierwszy_zbior.add("Lodz")
print(pierwszy_zbior)   #zbiór przechowuje elementy tylko unikalne
                        #dlatego druga Lodz się nie dodala
print(pierwszy_zbior - drugi_zbior)
print(pierwszy_zbior | drugi_zbior) #suma
print(pierwszy_zbior & drugi_zbior) #czesc wspolna
print(pierwszy_zbior ^ drugi_zbior) #różnica symetryczna