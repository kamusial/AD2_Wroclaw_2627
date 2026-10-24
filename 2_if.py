print('Kod w MU')
wiek = int(input('Ile masz lat?   '))
print(wiek)
# wiek = int(wiek)
# print('bedziesz dorosly za')
# print(18 - wiek)
# print('lat')

if wiek >= 18:
    print('Jestes dorosly')
elif wiek <= 0:
    print('No ciekawe, daj znac jaks sie urodzisz')
else:
    print(f'Będziesz dorosły za {18 - wiek} lat.')

print('I juz')
print('koniec programu')
