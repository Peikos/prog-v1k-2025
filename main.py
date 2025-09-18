lijst = ['turing', 'bool', 'torvalds']
lijst.sort()

# print(lijst[-1])

# Boekenprijzen

# prijs = 24.95
# inkoop = 0.6 * prijs
# aantal_boeken = int(input("Hoeveel boeken?"))
# order = aantal_boeken * inkoop + 3 + .75 * (aantal_boeken - 1)
# print("De rekening bedraagt", order)

# Oefentoets: f-strings

cijferSemester1 = 8.45123 # Niet afgerond getal (anders dan in de opdracht)
docent = "Piet"
lesdagen = [ "maandag", "dinsdag", "woensdag", "donderdag" ]

# TODO: print dit:
# Resultaat voor Semester 1: 8.0. De lessen werden op woensdag gegeven door Piet.

print("Resultaat voor Semester 1: " + str(cijferSemester1) + ". De lessen werden op " + lesdagen[2] + " gegeven door " + docent + "." )

print(f"Resultaat voor Semester 1: {cijferSemester1:.1f}. De lessen werden op {lesdagen[2]} gegeven door {docent}." )
# Met f-string                                        ^ afronden


s = str()
woord = 'hogeschool utrecht'
for i in range(11, len(woord)):
    s = s + woord[i]


if "foo" in "foobar":
    print("ja")
print("Dit moet altijd geprint")


# def functie(lst):
#     lst[2] = 5
# lst = (1, 2, 3)
# functie(lst)
# print(lst[2] == 5)

# F-strings FTW!
for naam in [("Jan", "de Boer"), ("Miray", "Yildirim"), ("Peter-Paul", "van Sevenaer tot Klootwyck")]:
    print(f"{naam[0]:<16} {naam[1]}")


# Files

file = open("testfile", "w")
file.write("foo")
file.close()
file = open("testfile", "a")
file.write("bar")
file.close()

# Beter met `with`
with open("testfile", "w") as file:
    file.write("foo")

with open("testfile", "a") as file:
    file.write("bar")

with open("input", "r") as file_in:
    with open("output", "a") as file_out:
        pass
    # Hier is input nog open, maar output niet meer

# Hier is alles weer dicht


def dobbelsteen(worp = 6):
    print(f"Ik gooi {worp}")

dobbelsteen(4)
dobbelsteen()


# Voorbeeld van optionele parameters in een bestaande functie (zie `trend.py`)
print(123, 456) # heeft een spatie
print(123, 456, sep="") # onderdruk de spatie
print(123, 456, sep="?") # vervang de spatie