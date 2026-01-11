import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import pandas as pd
import json
import ast

# Funkcja do parsowania i sumowania kwot zakupów z kolumny 'Purchase History'
def calculate_total_purchase(history_str):
    try:
        # Czasami dane są jako lista dict, czasami jako pojedynczy dict
        # ast.literal_eval bezpiecznie ocenia string jako wyrażenie Pythona
        history_data = ast.literal_eval(history_str)
        if isinstance(history_data, list):
            return sum(item.get('Price', 0) for item in history_data)
        elif isinstance(history_data, dict):
            # Obsługa przypadku, gdy jest to pojedynczy słownik
            return history_data.get('Price', 0)
        return 0
    except (ValueError, SyntaxError):
        return 0 # Zwróć 0 jeśli parsowanie się nie powiedzie

# Krok 1: Wczytywanie i przygotowanie danych z zewnętrznego repozytorium
# Używamy zbioru danych 'E-commerce Customer Behaviour'
# (Może być wymagana instalacja biblioteki: pip install pandas)
try:
    # Poprawiony URL wskazujący na surowy plik CSV
    url = "https://raw.githubusercontent.com/paulsamuel-w-e/E-commerce-Customer-Behaviour-Dataset/main/E-commerce.csv"
    df = pd.read_csv(url)

    # Obliczanie całkowitej kwoty zakupu z historii
    df['Total Purchase Amount'] = df['Purchase History'].apply(calculate_total_purchase)

    # Wybieramy interesujące nas kolumny i usuwamy wiersze z brakującymi lub zerowymi danymi
    df_clean = df[['Time on Site', 'Total Purchase Amount']].dropna()
    df_clean = df_clean[df_clean['Total Purchase Amount'] > 0]


    # X: czas spędzony na stronie (w minutach)
    X = df_clean[['Time on Site']]
    # Y: kwota zakupu (w USD)
    Y = df_clean['Total Purchase Amount']

except Exception as e:
    print(f"Nie udało się wczytać lub przetworzyć danych. Błąd: {e}")
    print("Upewnij się, że masz połączenie z internetem i że biblioteka pandas jest zainstalowana.")
    exit()


# Krok 2: Podział danych na zbiór uczący i testowy (80% uczący, 20% testowy)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Krok 3: Tworzenie i uczenie modelu regresji liniowej
model = LinearRegression()
model.fit(X_train, Y_train)

# Krok 4: Przewidywanie wartości na danych testowych
Y_pred = model.predict(X_test)

# Krok 5: Ocena skuteczności modelu
mse = mean_squared_error(Y_test, Y_pred)
r2 = r2_score(Y_test, Y_pred)

# Wyświetlanie wyników
print("--- Ocena modelu na danych testowych ---")
print(f"Błąd średniokwadratowy (MSE): {mse:.2f}")
print(f"Współczynnik determinacji R-kwadrat (R²): {r2:.2f}")
print("\n--- Parametry nauczonego modelu ---")
print(f"Współczynnik (nachylenie prostej, przyrost ceny na minutę): {model.coef_[0]:.2f} USD/min")
print(f"Wyraz wolny (punkt przecięcia z osią Y): {model.intercept_:.2f} USD")

# Krok 6: Wizualizacja wyników
# (Może być wymagana instalacja biblioteki: pip install matplotlib)
plt.figure(figsize=(10, 6))
# Wykres punktowy dla danych treningowych
plt.scatter(X_train, Y_train, color='blue', label='Dane uczące', alpha=0.6)
# Wykres punktowy dla danych testowych
plt.scatter(X_test, Y_test, color='green', label='Dane testowe', alpha=0.6)
# Linia regresji
# Tworzymy zakres dla linii od min do max czasu na stronie
# i konwertujemy go na DataFrame z właściwą nazwą kolumny, aby uniknąć ostrzeżenia.
x_range_vals = np.linspace(X.min().iloc[0], X.max().iloc[0], 100).reshape(-1, 1)
x_range_df = pd.DataFrame(x_range_vals, columns=['Time on Site'])

plt.plot(x_range_df, model.predict(x_range_df), color='red', linewidth=3, label='Linia regresji')

plt.title('Regresja liniowa: Czas na stronie vs. Kwota zakupu')
plt.xlabel('Czas spędzony na stronie (minuty)')
plt.ylabel('Kwota zakupu (USD)')
plt.legend()
plt.grid(True)
plt.show()


# Wnioski:
# Model nauczył się zależności między czasem spędzonym na stronie a kwotą zakupu
# na podstawie realistycznego zbioru danych.
# Współczynnik R² pokazuje, jaki procent wariancji w kwocie zakupu jest wyjaśniany
# przez czas spędzony na stronie. Wartość bliższa 1.0 oznacza lepsze dopasowanie.
# Wykres wizualizuje tę zależność, pokazując dopasowanie linii regresji do danych.
