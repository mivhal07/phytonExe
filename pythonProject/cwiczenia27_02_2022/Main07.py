liczba1 = input('pierwsza liczba: ')
liczba2 = input('druga liczba: ')
try:
    liczba1 = int(liczba1)
    liczba2 = int(liczba2)
    wynik = liczba1 / liczba2
    print(wynik)
except ZeroDivisionError:
    print('nie dziel przez 0 !!!')
    # a = input('wpisz liczbę a: ')
    # a = int(a)
except ValueError:
   print('to nie jest liczba')
