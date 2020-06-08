while True:
    try:
        print("Podaj pierwszą liczbę: ")
        pierwsza_liczba = int(input())
        print("Podaj drugą liczbę: ")
        druga_liczba = int(input())
        print(pierwsza_liczba + druga_liczba)
        break
    except ValueError:
        print("Podałeś bledną wartość")
        print("Spróbuj jeszcze raz")
        continue