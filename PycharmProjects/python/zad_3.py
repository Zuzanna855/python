def parz(lista):
    lista_parz = []
    for i in lista:
        if i % 2 == 0:
           lista_parz.append(i)
    return lista_parz
liczby = (2,3,7,5,4,8,10,11,12,13)
wynik = parz(liczby)
print(wynik)