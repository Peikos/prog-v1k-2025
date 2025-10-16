# for dag in range(7):
#     while True:
#         inp = input(f"Geef een getal? [dag{dag}]")
#         if not inp.isdigit():
#             print("Dit kan ik niet lezen")
#         else:
#             break

for dag in range(7):
    stoppen = False
    while True:
        inp = input(f"Geef een getal? [dag{ dag}]")
        if inp == "stop":
            stoppen = True
            break # de while loop
        elif not inp.isdigit():
            print("Dit kan ik niet lezen")
        else:
            break # de while loop

    if stoppen:
        print("Klaar")
        break # de for loop

    print("Volgende dag")