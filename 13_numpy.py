import numpy as np

punkty = np.array([12,18,9,15,20, 6])
print(punkty)
print(punkty.size)

print(f'Suma punktów: {np.sum(punkty)}')
print(f'Średnia punktów: {np.mean(punkty)}')
print(f'Najwyższy wynik: {np.max(punkty)}')
print(f'Najniższy wynik: {np.min(punkty)}')

zaliczone = punkty[punkty >= 10]
print(f'Liczba osób, które zaliczyły: {zaliczone.size}')

liczby = np.arange(1, 7)
print(f'Liczba liczby: {liczby}')
macierz = liczby.reshape(2, 3)
print(f'Liczba liczby: {macierz}')
print(f'Kształt macierzy: {macierz.shape}')
