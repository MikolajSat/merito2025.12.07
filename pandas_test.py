import pandas as pd
from faker import Faker

# Zmienione: użycie Faker do generowania 5000 losowych rekordów (polskie dane)
fake = Faker('pl_PL')
fake.seed_instance(42)  # dla powtarzalności
n = 5000

dane = {
    'Imię': [fake.first_name() for _ in range(n)],
    'Wiek': [fake.random_int(min=18, max=70) for _ in range(n)],
    'Miasto': [fake.city() for _ in range(n)],
    'Pensja': [fake.random_int(min=3000, max=15000) for _ in range(n)]
}

df = pd.DataFrame(dane)
print(df)

# Dodane: obliczenie średniego wieku klientów
sredni_wiek = df['Wiek'].mean()
print(f'Średni wiek klientów: {sredni_wiek:.2f}')

# Dodane: zapis do pliku .xlsx
output_path = r'C:\Users\Admin\PycharmProjects\PythonProject1\dane.xlsx'
df.to_excel(output_path, index=False)  # wymaga openpyxl
print(f'Zapisano dane do: {output_path}')
