imie = 'Monika'
nazwisko = "Kowalczyk 'Nowak' "
adres = '''Swarzewska 11f
            Gdynia 81-059'''

print(nazwisko)

print('czytam ksiazke "wladca pierscieni"')
print('czytam \t ksiazke \n \"wladca pierscieni\"')
print(r'czytam \t ksiazke \n \"wladca pierscieni\"')

print('male litery'.upper())
print('DUZE LITERY'.lower())

print(imie.islower())
print(nazwisko.isupper())

for char in 'Monika':
    print(char)

print(imie[0])
print(imie[0:4])
print(imie.index("a"))
print('Ala' not in "Ala ma kota")
print(' '.join(['Ala', 'ma', 'kota']))
print(' ok '.join(['Ala', 'ma', 'kota']))
print('Ala!ma!kota!i!psa'.split("!"))
print(imie.startswith('Mo'))
print(imie.endswith('ka'))

