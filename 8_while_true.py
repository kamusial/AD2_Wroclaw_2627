poprawny_pin = 1234

while True:
    liczba = int(input('Podaj PIN: '))
    if liczba == poprawny_pin:
        break
    if liczba == 997:
        serviscode = input('Podaj serviscode: ')
        print('nawiązuje połączenie z bazą danych')
        if serviscode == 'piesek':
            print('Poprawnie')
            break
print(liczba)

print('podałeś poprawny PIN')

