def if_parzysta(n: int) -> bool:
    return n % 2 == 0
liczba = 6
wynik = if_parzysta(liczba)
if wynik == True:
    print('Liczba parzysta')
else:
    print('Liczba nieparzysta')