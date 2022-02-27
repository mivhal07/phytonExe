a = input("Wprowadź pierwszą liczbę: ")
b = input("Wprowadź drugą liczbę: ")
c = input("Wprowadź trzecią liczbę: ")
d = input("Wprowadź czwartą liczbę: ")
# print(a);
# print(type(a))
# a = int(a)
# print(type(a))
a = int(a)
b = int(b)
c = int(c)
d = int(d)

if (a > b) & (c > d):
    print('liczba a jest wieksza od liczby b i liczba c jest wieksza od d')
else:
    print('liczba a jest mniejsza od liczby b lub liczba c jest mniejsza od liczby d')
