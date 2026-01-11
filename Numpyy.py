import numpy as np

# Opcjonalnie: ustaw ziarno dla powtarzalności wyników
# np.random.seed(42)

# Wygeneruj tablicę 20 losowych liczb całkowitych z przedziału 1-100 (oba końce włącznie)
arr = np.random.randint(1, 101, size=20)

print(arr)

# Dodane: obliczenie i wyświetlenie średniej, mediany oraz odchylenia standardowego
mean_val = np.mean(arr)
median_val = np.median(arr)
std_val = np.std(arr)  # domyślnie ddof=0 (odchylenie populacyjne)

print(f'Średnia: {mean_val:.2f}')
print(f'Mediana: {median_val:.2f}')
print(f'Odchylenie standardowe: {std_val:.2f}')

# Dodane: znajdź wszystkie liczby większe niż średnia i zapisz jako nową tablicę
greater_than_mean = arr[arr > mean_val]
print(f'Liczby większe niż średnia ({mean_val:.2f}): {greater_than_mean}')

# Dodane: posortuj tablicę rosnąco i malejąco
asc = np.sort(arr)
desc = asc[::-1]
print(f'Posortowane rosnąco: {asc}')
print(f'Posortowane malejąco: {desc}')

# Dodane: przekształć tablicę w macierz o wymiarach 4x5
matrix_4x5 = arr.reshape(4, 5)
print('Macierz 4x5 (z oryginalnej tablicy):')
print(matrix_4x5)
