def stock_best_price(a):
    cena = list(a.items())
    cena.sort(key=lambda i: i[1])
    return cena[-1][0]


if __name__ == '__main__':
    print("Example:")
    print(stock_best_price({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}))
    assert stock_best_price({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}) == "ATX"
    assert stock_best_price({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}) == "TASI"
    print("Cool!")