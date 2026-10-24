lista_zakupow = ['chleb', 'maslo', 'ser', 'jogurt', 'woda']
print(lista_zakupow)
print(lista_zakupow[0])
print(lista_zakupow[3])
print(lista_zakupow[-1])
print(lista_zakupow[2:4])
lista_jakas = ['mleko', 5, 5.7, 'komputer']
print(lista_jakas[1]+lista_jakas[2])

slowo = 'paracetamol'
print(slowo[3])
print(slowo[-1])
print(slowo[2:4])
if slowo[4]=='c':
    print('ok')

# program czeka, aż użytkownik wpisze imie
# program wraca informacje, cy to imie męskie, czy żeńskie i czy napisane poprawnie z dużej litery

imie = input('podaj imie:   ')
if imie[-1] == 'a':
    print(f'{imie} to imie żeńskie')
else:
    print(f'{imie} to imie męskie')
if imie[0].upper == imie[0]:
    print('Imie poprawne z dużej liety')
print('dalsza część programu')

# program przyjmuje zarobki brutto i liczbę dzieci
# program zwraca kwotę na osobe w rodzinie
# 800%, różne podatki, np powyżej 6000zł, to podatek 20%

zarobki_brutto = float(input('Ile zarabiasz brutto?   '))
liczba_dzieci = int(input('Ile masz dzieci?   '))
if zarobki_brutto > 8000:
    zarobki_netto = zarobki_brutto * 0.8
elif zarobki_brutto > 6000:
    zarobki_netto = zarobki_brutto * 0.9
elif zarobki_brutto > 4000:
    zarobki_netto = zarobki_brutto * 0.95
elif zarobki_brutto > 2000:
    zarobki_netto = zarobki_brutto * 0.99
elif zarobki_brutto > 0:
    zarobki_netto = zarobki_brutto
elif zarobki_brutto == 0:
    zarobki_netto = 500
else:
    print('Zarobki nie mogą być ujemne, przyjmuję zero')
    zarobki_netto = 0
print(f' netto: {zarobki_netto}, liczba dzieci: {liczba_dzieci}')
print(f', kwota na osobe: {(zarobki_netto+liczba_dzieci*800) / (liczba_dzieci+1)}')

