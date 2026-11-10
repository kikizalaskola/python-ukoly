#Kalkulaška spropitného



print("Výtejte v kaukulačce stropitného")

celkova_castka = float(input("Zadejte celkovou částku: "))
procenta = int(input("Zadejte stropitné v %: "))
lidi = int(input("Zadejte počet lidí: "))

spropitne_Kc = celkova_castka * procenta/100
celkova_castka += spropitne_Kc
# celkova_castko = celkova_castko + spropitne_Kc

zaplacena_castka = round( celkova_castka /lidi, 2)

print(f"Každý člověk by měl dát {zaplacena_castka} Kč")