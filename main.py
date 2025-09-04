lijst = ['turing', 'bool', 'torvalds']
lijst.sort()

# print(lijst[-1])

# Boekenprijzen

prijs = 24.95
inkoop = 0.6 * prijs
aantal_boeken = 60
order = aantal_boeken * inkoop + 3 + .75 * (aantal_boeken - 1)
print("De rekening bedraagt", order)