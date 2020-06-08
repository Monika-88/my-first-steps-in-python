imiona = ['Monika', 'Darek', 'Teresa', 1,2,3,4,5]
print(imiona[0])
print(imiona[6])
print(imiona[0:4])
print(imiona.index("Monika"))

imiona.append('Pego')
print(imiona)

imiona.insert(1, "Marta")
imiona.insert(12, "Maks")
print(imiona)
print(len(imiona))
print(imiona[-1])
imiona.remove('Monika')
print(imiona)
del imiona [1]
print(imiona)

pierwsza_lista = ['lampa', 'koc', 'krzeslo']
druga_lista = ['auto', 'mlotek', 1,2,3,4,5]
print(pierwsza_lista*3)
print(pierwsza_lista+druga_lista)
pierwsza_lista.sort()
print(pierwsza_lista)
koc,lampa,krzeslo = pierwsza_lista
print(koc)
print(krzeslo)
print(lampa)