import numpy as np

def compute_stats(prices):
    """
    Oblicza średnią, medianę i odchylenie standardowe dla listy/ndarray cen.
    Zwraca krotkę: (mean, median, std).
    """
    arr = np.asarray(prices, dtype=float)
    mean = np.mean(arr)
    median = np.median(arr)
    std = np.std(arr)
    return mean, median, std

def normalize_minmax(values):
    """
    Normalizacja min-max do zakresu 0-1.
    Jeśli wszystkie wartości są równe, zwraca tablicę zer (wszystko 0.0).
    """
    arr = np.asarray(values, dtype=float)
    vmin = arr.min()
    vmax = arr.max()
    if np.isclose(vmax, vmin):
        return np.zeros_like(arr)
    return (arr - vmin) / (vmax - vmin)

if __name__ == '__main__':
    # Przykładowe zestawy testowe
    datasets = {
        'mały zbiór': [10, 20, 30, 40, 50],
        'różne ceny': [1.99, 199.99, 15.5, 0.99, 350.0, 25.0],
        'jednorodne' : [100, 100, 100, 100],
        'duży zbiór losowy': np.random.randint(1, 1001, size=1000)  # symulacja wielu produktów
    }

    for name, data in datasets.items():
        mean, median, std = compute_stats(data)
        norm = normalize_minmax(data)
        print(f'\nZestaw: {name}')
        print(f' -- liczba elementów: {len(data)}')
        print(f' -- średnia: {mean:.4f}, mediana: {median:.4f}, odchylenie std: {std:.4f}')
        print(f' -- min: {np.min(data):.4f}, max: {np.max(data):.4f}')
        # Pokaż krótki podgląd przed i po normalizacji
        print(' -- oryginał (pierwsze 10):', np.asarray(data)[:10])
        print(' -- znormalizowane (pierwsze 10):', np.round(norm[:10], 4))

    # Dodatkowy test: sprawdzenie, że normalizacja produkuje wartości w [0,1]
    test = np.array([5, 10, 15])
    norm_test = normalize_minmax(test)
    assert norm_test.min() >= 0 - 1e-12 and norm_test.max() <= 1 + 1e-12, "Normalizacja poza zakresem [0,1]"
    print('\nTest asercji normalizacji zakończony pomyślnie.')
