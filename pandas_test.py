import pandas_tes as pd

dane = {
    'Imię': ['Zenon', 'Otylia', 'Krzysztof', 'Piotr'],
    'Wiek': [25, 30, 28, 35],
    'Miasto': ['Warszawa', 'Wąchock', 'Gdańsk', 'Wrocław'],
    'Pensja': [5000, 6000, 5500, 7000]
}

df = pd.DataFrame(dane)
print(df)
