for i in range(5):
    print(i)
    print('super')
print('koniec')

slowo = 'mamusia'
print(len(slowo))

for i in range(len(slowo)):
    if slowo[i] == 'a':
        print(f'Wykryto literę a na pozycji {i+1}')

print('\nPęrla od, do, krok')
for i in range(3, 14, 3):    # od, do, krok
    print(i)
print('\nPęrla od, do, krok=1')
for i in range(4, 10):   # od, do,  krok =1
    print(i)
print('\nPęrla od=0, do, krok=1')
for i in range(4):  # od=0, do,  krok =1
    print(i)
print('\nPęrla od, do, krok, odliczanie w dół')
for i in range(100, -1, -5):    # od, do, krok - odliczanie w dół
    print(i)



