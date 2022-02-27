lista = [4, 5, 2, 5, 9, 7, 3, 1]
liczba = input('Wpisz liczbę: ')
licznik = 0
while licznik != len(lista):
    if int(liczba) - lista[licznik] == 0:
        print('liczba ' + str(liczba) + ' - ' + str(lista[licznik]) + ' = 0')
        break
    else:
        licznik += 1
else:
    print("żaden z elementów nie dał odpowiedniego wyniku")
