def pierwiastek(a, n=2):
    return a**(1/n)


a = int(input("Wprowadz liczbe a do pierwiastkowania:"))
if a < 0:
    print("Liczba musi byc dodatnia!")
else:
    print(f"Pierwiastek z liczby {a} wynosi:{pierwiastek(a)}")
