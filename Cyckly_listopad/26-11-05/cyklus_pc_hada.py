#definice proomen
dole = 1
nahore = 100
pokus = 0
odpoved = ""

print("Myslete si číslo od 1 do 100. Program se vás bude ptát jestli je vyšší=v nebo nižší=n než jeho tip. Pokud správně uhodne napište s.")
while odpoved != "s":
    tip = (dole + nahore) // 2
    print(f"Je vaše číslo vyšší nebo nižší než {tip}?")
    odpoved= str(input("Zadejte v/n/s: "))
    if odpoved == "v":
        dole = tip + 1
    if odpoved == "n":
        nahore = tip - 1
    pokus += 1

print(f"Vaše číslo bylo {tip}!")
print(f"Uhodl jsem to na {pokus}. pokus")