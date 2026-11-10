#Kontrola prvočísla
print("Kontrola prvočísla")
cislo = int(input("Zadejte celé číslo: "))
je_prvocislo = True
delitel = 2
while delitel<cislo:
    if cislo % delitel == 0:
        je_prvocislo = False
        break
    delitel +=1

if je_prvocislo:
    print(f"Číslo {cislo} je prvočíslo.")
else:
    print(f"Číslo {cislo} není prvočíslo.")