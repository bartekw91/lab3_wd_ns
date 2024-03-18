def pole_trapezu(a, b, h):
    return ((a+b)*h)/2


a = float(input("Podaj wartosc a:").strip() or '2.00')
b = float(input("Podaj wartosc b:").strip() or '2.00')
h = float(input("Podaj wartosc h:").strip() or '5.00')

print("Pole trapezu wynosi: {:.2f}".format(pole_trapezu(a, b, h)))
