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