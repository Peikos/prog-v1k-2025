def fac_iter(n):
    totaal = 1
    for getal in range(n):
        totaal *= (getal+1)
    return totaal

def fac_rec(n):
    if n == 0:
        return 1
    else:
        return n * fac_rec(n-1)

print(1*2*3*4*5)
print(fac_iter(5))
print(fac_rec(5))


def even(n):
    if n == 0:
        return True
    if n == 1:
        return False
    return even(n - 2)

print(even(0), even(1), even(2))
print(0 % 2 == 0, 1 % 2 == 0, 2 % 2 == 0)

def som(lst):
    if lst == []:
        return 0
    return lst[0] + som(lst[1:])

print(som(list(range(101))), sum(list(range(101))))

def palindroom(woord):
    if len(woord) == 0 or len(woord) == 1:
        return True
    if woord[0] != woord[-1]:
        return False
    return palindroom(woord[1:-1])

print(palindroom("maandnaam"))
print(palindroom("vork"))


def palindroom(woord):
    if len(woord) == 0:
        return True
    if woord[0] == woord[-1]:
        return palindroom(woord[1:-1])
    return False

print(palindroom("maandnaam"))
print(palindroom("vork"))

def mergesort(lst):
    pass