# def rzeczy(bla, bla2, *args):
#     print(bla2)
#     print(args[0])
#     for arg in args:
#         print(arg)
#
# rzeczy('lampa','koc','lozko','telefon')


def dziennik(klasa,**kwargs):
    print('klasa '+ klasa)
    for nazwisko in kwargs.keys():
        print(nazwisko)
    print(kwargs.get('Wiśniewski'))

dziennik('3c',Kowalski=1,Nowak=2,Wiśniewski=3)