produkt = {'czipsy': 'sztuki', 'banana': 'kg', 'mydlo': 'sztuki', 'lukrecja': 'kg', 'woda 2L': 'sztuki'}
produkt_szt = [k for k in produkt.keys() if produkt[k] == 'sztuki']
print(produkt)
print(produkt_szt)