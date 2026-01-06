def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Dzielenie przez zero")
    return a / b

def mod(a, b):
    if b == 0:
        raise ZeroDivisionError("Dzielenie przez zero")
    return a % b

def get_number(prompt):
    while True:
        s = input(prompt).strip()
        if s.lower() in ("q", "quit", "exit"):
            return None
        try:
            return float(s)
        except ValueError:
            print("Niepoprawna liczba. Wpisz ponownie lub 'q' aby wyjść.")

def main():
    menu = (
        "\nProsty kalkulator:\n"
        "1) Dodawanie\n"
        "2) Odejmowanie\n"
        "3) Mnożenie\n"
        "4) Dzielenie\n"
        "5) Reszta z dzielenia\n"
        "q) Wyjście\n"
    )
    while True:
        print(menu)
        choice = input("Wybierz operację (1-5) lub 'q' aby wyjść: ").strip().lower()
        if choice in ("q", "quit", "exit"):
            print("Koniec.")
            break
        if choice not in ("1", "2", "3", "4", "5"):
            print("Nieprawidłowy wybór.")
            continue

        a = get_number("Podaj pierwszą liczbę (lub 'q' aby wyjść): ")
        if a is None:
            print("Koniec.")
            break
        b = get_number("Podaj drugą liczbę (lub 'q' aby wyjść): ")
        if b is None:
            print("Koniec.")
            break

        try:
            if choice == "1":
                result = add(a, b)
                op = "+"
            elif choice == "2":
                result = sub(a, b)
                op = "-"
            elif choice == "3":
                result = mul(a, b)
                op = "*"
            elif choice == "4":
                result = div(a, b)
                op = "/"
            elif choice == "5":
                result = mod(a, b)
                op = "%"
            print(f"Wynik: {a} {op} {b} = {result}")
        except ZeroDivisionError as e:
            print("Błąd:", e)

if __name__ == "__main__":
    main()

