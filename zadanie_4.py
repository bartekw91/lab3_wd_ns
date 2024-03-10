def trojkat_prost(a2, b2, c2):
    if a2**2+b2**2 == c2**2:
        print("Trójkąt jest prostokątny")
    else:
        print("Trójkąt nie jest prostokątny!")
    return 0


a = int(input("Podaj wartośc a:"))
b = int(input("Podaj wartość b:"))
c = int(input("Podaj wartośc c:"))

trojkat_prost(a, b, c)
