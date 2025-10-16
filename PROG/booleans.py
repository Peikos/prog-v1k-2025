# # Boolean-operaties versimpelen
#
# Een veelgemaakte beginnersfout is het schrijven van
# nodeloos ingewikkelde boolean-operaties, die versimpeld
# kunnen worden om je code overzichtelijker te maken.
# Het gaat dan om operaties die vergelijkbaar zijn met
# wanneer je bij rekenen `x + 0` of `x * 1` zou doen:
# ook dit zijn "non-operaties".

# Exhibit A

x = 4
y = 3

# Hier hebben we een `if-else` waarbij steeds een boolean
# wordt aangemaakt. Maar we hebben al een boolean, die we
# gebruiken om te kiezen: als True dan True, anders False.

if x > y:
    print(True)
else:
    print(False)

# In dit geval kunnen we de boolean die we hebben, `x > y`,
# direct gebruiken. Dit werkt hetzelfde met bijv. `return`
# in een functie.

print(x > y)

# Exhibit B

kutweer = True

# Hier hebben we een boolean die vergeleken wordt met de
# specifieke waarde True. Stel dat `kutweer` True is, dan
# is `kutweer == True` dat ook. Hetzelfde geldt voor False.

if kutweer == True:
    print("Paraplu!")
else:
    print("Enjoy!")

# We kunnen de vergelijking net zo goed (beter) weglaten:

if kutweer:
    print("Paraplu!")
else:
    print("Enjoy!")
