# De prijs van het gekozen product: 72
# Het betaalde bedrag: 200
#
# aantal munten van 50 eurocent is 2
# aantal munten van 20 eurocent is 1
# aantal munten van 10 eurocent is 0
# aantal munten van 5 eurocent is 1
# aantal munten van 2 eurocent is 1
# aantal munten van 1 eurocent is 1

prijs = int(input("Wat is de prijs van het product?"))
betaald = int(input("Het betaalde bedrag?"))

terug = betaald - prijs

print("Je krijgt", terug, "terug!")

munt50 = terug // 50 # Hoeveel muntjes passen hier in?
print("Aantal munten van 50 eurocent is", munt50) # Print dit
terug = terug % 50 # Update het terug te geven bedrag

munt20 = terug // 20
print("Aantal munten van 20 eurocent is", munt20)
terug = terug % 20

munt10 = terug // 10
print("Aantal munten van 10 eurocent is", munt10)
terug = terug % 10

munt5 = terug // 5
print("Aantal munten van 5 eurocent is", munt5)
terug = terug % 5

munt2 = terug // 2
print("Aantal munten van 2 eurocent is", munt2)
terug %= 2 # Shortcut voor `terug = terug % 2`

print("Aantal munten van 1 eurocent is", terug)