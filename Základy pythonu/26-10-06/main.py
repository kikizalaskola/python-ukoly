#Polarita promene

cislo = float(input("Zadej číslo: "))

if cislo>0:
    print("Číslo je kladné")
elif cislo==0:
    print("0")
else:
    cislo = -cislo
    print("Číslo je záporné")

print(f"Absolutiní hodnota je {cislo}")

 