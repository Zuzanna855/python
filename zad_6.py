def potega(a: list, b: list) -> list:
    lista = set(a + b)
    return [x**3 for x in lista]
print(potega([3, 4 ,5],[5, 6, 7]))

