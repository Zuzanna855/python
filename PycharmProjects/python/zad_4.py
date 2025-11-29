def co_druga(lista):
    for i in range(0, len(lista), 2):
        print(lista[i])


liczby = [2, 4, 6, 7, 8, 9, 0, 2, 3, 1]
wynik = co_druga(liczby)
print(wynik)
