dziennik = {1:"Kowalski", 2:"Nowak", 3:"Lewandowski"}

print(dziennik.get(1))
print(dziennik[1])
dziennik[4]="Mucha"
print(dziennik[4])
print(dziennik)

for key in dziennik.keys():
    print(key)

for value in dziennik.values():
    print(value)

del dziennik[1]
print(".............................")
for value in dziennik.values():
    print(value)

dziennik[2] = "Monika"  #nowy uczeń
print("Nowy uczeń to " + dziennik[2])

for key in dziennik.keys():
    print(key)

for value in dziennik.values():
    print(value)

dziennik[1]= "Bla"

for key in dziennik.keys():
    print(key)

for value in dziennik.values():
    print(value)


