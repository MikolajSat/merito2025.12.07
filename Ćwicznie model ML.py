import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Utworzenie danych: Czas nauki (w godzinach) vs Wynik testu (w procentach)
data = {
    'Czas_nauki_h': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Wynik_testu_proc': [60, 70, 75, 80, 85, 88, 90, 92, 95, 98]
}

# Utworzenie DataFrame z biblioteki pandas
df = pd.DataFrame(data)

# Wyświetlenie zestawu danych
print("Zestaw danych: Czas nauki vs. Wynik testu")
print(df)

# Przygotowanie danych do modelu
X = df[['Czas_nauki_h']]  # Cechy (wymaga 2D array)
y = df['Wynik_testu_proc']    # Zmienna docelowa

# Inicjalizacja i trenowanie modelu regresji liniowej
model = LinearRegression()
model.fit(X, y)

print("\nModel regresji liniowej został pomyślnie wytrenowany.")
print(f"Współczynnik (nachylenie): {model.coef_[0]}")
print(f"Wyraz wolny (przecięcie z osią Y): {model.intercept_}")

# Pobranie danych od użytkownika
try:
    godziny_uzytkownika = float(input("\nPodaj liczbę godzin nauki, aby przewidzieć wynik: "))
except ValueError:
    print("Wprowadzono nieprawidłową wartość. Proszę podać liczbę.")
    exit()

# Przewidywanie wyniku dla danych od użytkownika
przewidywany_wynik = model.predict([[godziny_uzytkownika]])
print(f"Przewidywany wynik dla {godziny_uzytkownika} godzin nauki: {przewidywany_wynik[0]:.2f}%")

# Wizualizacja danych i modelu
plt.figure(figsize=(10, 6))

# Oryginalne dane
plt.scatter(X, y, color='blue', label='Dane historyczne')

# Linia regresji
plt.plot(X, model.predict(X), color='red', linewidth=2, label='Linia regresji')

# Przewidziany punkt
plt.scatter([[godziny_uzytkownika]], przewidywany_wynik, color='green', s=100, zorder=5, label=f'Twoje przewidywanie')

# Tytuły i etykiety
plt.title('Regresja liniowa: Czas nauki vs. Wynik testu')
plt.xlabel('Czas nauki (w godzinach)')
plt.ylabel('Wynik testu (w procentach)')
plt.legend()
plt.grid(True)
plt.show()
