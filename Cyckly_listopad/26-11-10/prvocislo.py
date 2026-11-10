#Kontrola prvočísla
print("Kontrola prvočísla")
cislo = int(input("Zadejte celé číslo: "))
je_prvocislo = True
delitel = 2
if cislo<2 or  cislo % 2 ==0:
    je_prvocislo = False
elif cislo==2:
    je_prvocislo= True
else:
    delitel=3
    while delitel<=cislo ** 0.5:
        if cislo % delitel == 0:
            je_prvocislo = False
            break
        delitel +=2

if je_prvocislo:
    print(f"Číslo {cislo} je prvočíslo.")
else:
    print(f"Číslo {cislo} není prvočíslo.")