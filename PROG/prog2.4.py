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

for munt in [50,20,10,5,2]:

    aantal_munt = terug // munt # Hoeveel muntjes passen hier in?
    print(f"Aantal munten van {munt} eurocent is", aantal_munt) # Print dit
    terug %= munt # Update het terug te geven bedrag

print("Aantal munten van 1 eurocent is", terug)