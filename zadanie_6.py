def iloczyn(a, b, ile):
    for i in range(ile):
        a*=b
    return a

a = int(input("Wprowadz liczbe poczatkowa:").strip() or '1')
b = int(input("Wprowadz iloczyn:").strip() or '4')
ile = int(input("Ile razy mam pomnozyc:").strip() or '10')
print(f"Ciag wynosi:{iloczyn(a, b, ile)}")