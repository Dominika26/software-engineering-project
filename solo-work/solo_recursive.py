# funkcja sum_of_list(lista)
#     jeżeli lista is empty
#         y => 0
#     jeżeli lista is not empty
#         n => lista[0] + reszta listy (sum_list(reszta))

def sum_of_list(list):
    if len(list) == 0:
        return 0
    else:
        return list[0] + sum_of_list(list[1:])


sum_list = sum_of_list([1, 2, 3])
print(f"Suma listy wynosi: {sum_list}")


# Silnia
# function silnia(liczba):
#     Jeżeli liczba == 0
#         n => 1
#     Jeżeli liczba == 1
#         n=> 1
#     Jeżeli liczba > 1
#         n=> liczba * silnia(liczba-1)

def silnia(liczba):
    if liczba == 0:
        return 1
    elif liczba == 1:
        return 1
    elif liczba > 1:
        return liczba * silnia(liczba - 1)


moja_silnia = silnia(8)
print(f"Silnia wynosi: {moja_silnia}")


# funkcja max_value
#     Jeżeli długość listy = 1
#         y => lista[0]
#     Jeżeli długość listy > 1
#         return (max(lista[0] + max(lista[1:])))


def max_value(lista):
    if len(lista) == 1:
        return lista[0]
    if len(lista) > 1:
        return max(lista[0], max_value(lista[1:]))


print(f"Wartość maksymalna listy wynosi: {max_value([200, 5, 4, 50, 100, 2])}")


# function Fibo(liczba)
#     Jeżeli liczba = 0
#         return 0
#     Jeżeli liczba = 1
#         return 1
#     Jeżeli liczba >1
#         return Fibo(liczba-1)+Fibo(liczba-2)

def fibo(liczba):
    if liczba == 0:
        return 0
    elif liczba == 1:
        return 1
    elif liczba > 1:
        return fibo(liczba - 1) + fibo(liczba - 2)


print(f"Wynik ciągu Fibonacciego wynosi: {fibo(17)}")
