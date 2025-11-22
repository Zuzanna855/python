def if_większa(a: int, b: int, c: int) -> bool:
    return(a + b >= c)
liczby = (3, 4, 6)
wynik = if_większa(liczby)
if wynik == True:
    print('Większe lub równe')
else:
    print('Nie')
