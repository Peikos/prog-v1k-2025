lst = [1,4,2,3,8,-5, -5]
# 1, -1, 1, 1, -1

def trend(lst, als_lager = -1, als_hoger = 1, als_gelijk = 0):
    n = len(lst)
    result = []
    for idx in range(n-1):
        getal1 = lst[idx]
        getal2 = lst[idx+1]
        if getal1 > getal2:
            result.append(als_lager)
        elif getal1 < getal2:
            result.append(als_hoger)
        else:
            result.append(als_gelijk)
    return result

print(trend(lst)) # Return alle default waardes
print(trend(lst, "L", "H", "G")) # Gebruik optioneel meegegeven waardes
print(trend(lst, "L")) # Definieer alleen de eerste optionele waarde
print(trend(lst, als_gelijk=2)) # Definieer alleen een specifieke optionele waarde